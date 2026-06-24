#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jommi Tomi - REST API Server for Node-based Workflow Management
نظام تومي جومي - خادم REST API لإدارة سير العمل العقدي

This Flask-based API server provides endpoints for managing the complete workflow,
allowing clients to submit projects, track progress, and retrieve results.

Version: 1.0
Author: Manus AI
Date: May 6, 2026
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
from typing import Dict, Any, Optional
import logging

# Import the orchestrator from the main module
from jomi_tomi_node_orchestrator import WorkflowOrchestrator, ArtStyle


# ============================================================================
# FLASK APPLICATION SETUP
# ============================================================================

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# In-memory storage for active projects (in production, use a database)
active_projects: Dict[str, Dict[str, Any]] = {}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def validate_project_data(data: Dict[str, Any]) -> tuple[bool, Optional[str]]:
    """Validate the project data."""
    required_fields = [
        "child_name",
        "child_age",
        "child_gender",
        "image_path",
        "story_theme"
    ]
    
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    
    # Validate age
    try:
        age = int(data["child_age"])
        if age < 1 or age > 18:
            return False, "Child age must be between 1 and 18"
    except ValueError:
        return False, "Child age must be a number"
    
    # Validate gender
    if data["child_gender"].lower() not in ["male", "female", "other"]:
        return False, "Gender must be 'male', 'female', or 'other'"
    
    return True, None


def create_response(status: str, message: str, data: Optional[Dict] = None, code: int = 200) -> tuple[Dict, int]:
    """Create a standardized API response."""
    response = {
        "status": status,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }
    
    if data:
        response["data"] = data
    
    return response, code


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return create_response("success", "API is healthy", {
        "service": "Jommi Tomi API Server",
        "version": "1.0",
        "status": "running"
    })


@app.route('/api/v1/projects', methods=['POST'])
def create_project():
    """Create a new project and start the workflow."""
    try:
        data = request.get_json()
        
        # Validate input
        is_valid, error_message = validate_project_data(data)
        if not is_valid:
            return create_response("error", error_message, code=400)
        
        # Create orchestrator and execute workflow
        orchestrator = WorkflowOrchestrator(f"project_{data['child_name']}")
        result = orchestrator.execute_workflow(data)
        
        # Store project information
        project_id = result.get("project_id")
        active_projects[project_id] = {
            "data": data,
            "result": result,
            "created_at": datetime.now().isoformat(),
            "status": result.get("status")
        }
        
        logger.info(f"Created project: {project_id}")
        
        return create_response(
            "success",
            "Project created and workflow started",
            {
                "project_id": project_id,
                "child_name": data["child_name"],
                "status": result.get("status"),
                "execution_summary": {
                    "total_nodes": result.get("total_nodes"),
                    "successful_nodes": result.get("successful_nodes"),
                    "failed_nodes": result.get("failed_nodes")
                }
            },
            code=201
        )
    
    except Exception as e:
        logger.error(f"Error creating project: {str(e)}")
        return create_response("error", f"Failed to create project: {str(e)}", code=500)


@app.route('/api/v1/projects/<project_id>', methods=['GET'])
def get_project(project_id: str):
    """Get project details and status."""
    if project_id not in active_projects:
        return create_response("error", f"Project not found: {project_id}", code=404)
    
    project = active_projects[project_id]
    
    return create_response(
        "success",
        "Project retrieved successfully",
        {
            "project_id": project_id,
            "child_name": project["data"]["child_name"],
            "status": project["status"],
            "created_at": project["created_at"],
            "result": project["result"]
        }
    )


@app.route('/api/v1/projects/<project_id>/status', methods=['GET'])
def get_project_status(project_id: str):
    """Get the current status of a project."""
    if project_id not in active_projects:
        return create_response("error", f"Project not found: {project_id}", code=404)
    
    project = active_projects[project_id]
    result = project["result"]
    
    return create_response(
        "success",
        "Project status retrieved",
        {
            "project_id": project_id,
            "status": project["status"],
            "progress": {
                "total_nodes": result.get("total_nodes"),
                "completed_nodes": result.get("successful_nodes"),
                "percentage": int((result.get("successful_nodes", 0) / result.get("total_nodes", 1)) * 100)
            },
            "execution_history": result.get("execution_history", [])
        }
    )


@app.route('/api/v1/projects', methods=['GET'])
def list_projects():
    """List all active projects."""
    projects = []
    
    for project_id, project_data in active_projects.items():
        projects.append({
            "project_id": project_id,
            "child_name": project_data["data"]["child_name"],
            "status": project_data["status"],
            "created_at": project_data["created_at"]
        })
    
    return create_response(
        "success",
        f"Retrieved {len(projects)} projects",
        {
            "total_projects": len(projects),
            "projects": projects
        }
    )


@app.route('/api/v1/projects/<project_id>/outputs', methods=['GET'])
def get_project_outputs(project_id: str):
    """Get the output files and artifacts from a completed project."""
    if project_id not in active_projects:
        return create_response("error", f"Project not found: {project_id}", code=404)
    
    project = active_projects[project_id]
    
    # Simulated output files (in real implementation, these would be actual files)
    outputs = {
        "video": f"story_video_final_{project['data']['child_name']}.mp4",
        "character_sheet": f"character_sheet_{project['data']['child_name']}.png",
        "model_sheet": f"model_sheet_{project['data']['child_name']}.png",
        "book_cover": f"book_cover_{project['data']['child_name']}.png",
        "print_pages": [
            f"page_1_{project['data']['child_name']}.png",
            f"page_2_{project['data']['child_name']}.png",
            f"page_3_{project['data']['child_name']}.png"
        ],
        "social_media": {
            "reels": [
                f"reel_1_{project['data']['child_name']}.mp4",
                f"reel_2_{project['data']['child_name']}.mp4"
            ],
            "promotional_posts": [
                f"promo_1_{project['data']['child_name']}.png",
                f"promo_2_{project['data']['child_name']}.png"
            ]
        }
    }
    
    return create_response(
        "success",
        "Project outputs retrieved",
        {
            "project_id": project_id,
            "child_name": project["data"]["child_name"],
            "outputs": outputs
        }
    )


@app.route('/api/v1/art-styles', methods=['GET'])
def get_art_styles():
    """Get list of available art styles."""
    styles = [
        {
            "id": "pixar",
            "name": "Pixar Style",
            "description": "Modern Pixar 3D animation with exaggerated, expressive features"
        },
        {
            "id": "disney",
            "name": "Disney Style",
            "description": "Classic Disney animation with timeless character design"
        },
        {
            "id": "dreamworks",
            "name": "DreamWorks Style",
            "description": "DreamWorks animation with modern CGI rendering"
        },
        {
            "id": "studio_ghibli",
            "name": "Studio Ghibli Style",
            "description": "Hand-drawn animation style inspired by Studio Ghibli"
        },
        {
            "id": "anime",
            "name": "Anime Style",
            "description": "Japanese anime style with expressive eyes and features"
        }
    ]
    
    return create_response(
        "success",
        "Art styles retrieved",
        {"styles": styles}
    )


@app.route('/api/v1/story-themes', methods=['GET'])
def get_story_themes():
    """Get list of available story themes."""
    themes = [
        {
            "id": "magical_adventure",
            "name": "Magical Adventure",
            "description": "An epic journey through magical realms"
        },
        {
            "id": "underwater_quest",
            "name": "Underwater Quest",
            "description": "An adventure in the depths of the ocean"
        },
        {
            "id": "space_explorer",
            "name": "Space Explorer",
            "description": "A journey through the cosmos and distant planets"
        },
        {
            "id": "enchanted_forest",
            "name": "Enchanted Forest",
            "description": "Discovering secrets in an ancient enchanted forest"
        },
        {
            "id": "time_traveler",
            "name": "Time Traveler",
            "description": "Traveling through different time periods"
        }
    ]
    
    return create_response(
        "success",
        "Story themes retrieved",
        {"themes": themes}
    )


@app.route('/api/v1/documentation', methods=['GET'])
def get_documentation():
    """Get API documentation."""
    docs = {
        "title": "Jommi Tomi API Documentation",
        "version": "1.0",
        "endpoints": [
            {
                "method": "GET",
                "path": "/api/v1/health",
                "description": "Health check endpoint"
            },
            {
                "method": "POST",
                "path": "/api/v1/projects",
                "description": "Create a new project and start the workflow",
                "request_body": {
                    "child_name": "string",
                    "child_age": "integer",
                    "child_gender": "string (male/female/other)",
                    "image_path": "string",
                    "story_theme": "string",
                    "art_style": "string (optional, default: pixar)"
                }
            },
            {
                "method": "GET",
                "path": "/api/v1/projects",
                "description": "List all active projects"
            },
            {
                "method": "GET",
                "path": "/api/v1/projects/<project_id>",
                "description": "Get project details"
            },
            {
                "method": "GET",
                "path": "/api/v1/projects/<project_id>/status",
                "description": "Get project status and progress"
            },
            {
                "method": "GET",
                "path": "/api/v1/projects/<project_id>/outputs",
                "description": "Get project output files"
            },
            {
                "method": "GET",
                "path": "/api/v1/art-styles",
                "description": "Get available art styles"
            },
            {
                "method": "GET",
                "path": "/api/v1/story-themes",
                "description": "Get available story themes"
            }
        ]
    }
    
    return create_response(
        "success",
        "Documentation retrieved",
        docs
    )


# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return create_response("error", "Endpoint not found", code=404)


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(error)}")
    return create_response("error", "Internal server error", code=500)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == '__main__':
    logger.info("Starting Jommi Tomi API Server...")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )
