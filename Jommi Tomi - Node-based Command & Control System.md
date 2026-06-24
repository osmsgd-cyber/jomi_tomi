# Jommi Tomi - Node-based Command & Control System
# نظام تومي جومي - النظام العقدي المتكامل

A comprehensive, automated system for transforming children's photos into Pixar-style stories with multiple outputs including printed books, animated videos, and social media content.

نظام متكامل وآلي لتحويل صور الأطفال إلى قصص بأسلوب Pixar مع مخرجات متعددة تشمل كتبًا مطبوعة وفيديوهات متحركة ومحتوى وسائل التواصل الاجتماعي.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [File Structure](#file-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

Jommi Tomi is an innovative platform that leverages artificial intelligence to create personalized, Pixar-style stories for children. The system uses a node-based architecture (Command & Control System) to orchestrate a complex workflow that includes:

1. **Character Generation** - Transform a child's photo into a Pixar-style character
2. **Story Creation** - Generate a unique story based on the child's age and preferences
3. **Scene Generation** - Create cinematic scenes featuring the child's character
4. **Video Production** - Animate scenes into a short film
5. **Audio Integration** - Add voice-over, sound effects, and music
6. **Social Media Content** - Generate promotional materials and reels
7. **Publishing** - Publish to Jommi Tomi platforms

---

## ✨ Features

### Core Features
- **Automated Workflow** - Complete end-to-end automation from photo to final product
- **Character Consistency** - Maintains character consistency across all scenes using advanced AI techniques
- **Multiple Art Styles** - Support for Pixar, Disney, DreamWorks, Studio Ghibli, and Anime styles
- **Multi-format Output** - Generate videos (16:9), print materials (A4), and social media content
- **Customizable Prompts** - Extensive prompt library for fine-tuning AI outputs
- **REST API** - Full-featured API for integration with external systems

### Technical Features
- **Node-based Architecture** - Modular, scalable design with 12 specialized nodes
- **Orchestration System** - Intelligent workflow management and error handling
- **Logging & Monitoring** - Comprehensive logging for debugging and monitoring
- **CORS Support** - Cross-origin resource sharing for web integration
- **JSON Configuration** - Easy configuration through JSON files

---

## 🏗️ System Architecture

The system is built on a node-based architecture with 12 specialized nodes:

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. Project Management (Initialization)                          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2. Client Data Input (Collect information)                      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 3. Image Analysis (Extract features)                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 4. Art Style Selection (Choose style)                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 5. Story Script Generation (Create narrative)                   │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 6. Character Generation (Transform photo to character)          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 7. Still Scene Generation (Create scenes)                       │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 8. Frame Approval (Client review)                               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
        ┌─────────────────────┴─────────────────────┐
        ↓                                           ↓
┌──────────────────────┐              ┌──────────────────────┐
│ 9. Video Generation  │              │ Print Preparation    │
└──────────────────────┘              └──────────────────────┘
        ↓                                           ↓
┌──────────────────────┐                           │
│ 10. Audio Integration│                           │
└──────────────────────┘                           │
        ↓                                           ↓
        └─────────────────────┬─────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 11. Social Media Content Generation                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 12. Publishing (Deploy to platforms)                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Flask and dependencies

### Step 1: Clone or Download the Repository
```bash
git clone https://github.com/your-repo/jommi-tomi.git
cd jommi-tomi
```

### Step 2: Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
python jomi_tomi_node_orchestrator.py
```

---

## 🚀 Usage

### Using the Orchestrator Directly

```python
from jomi_tomi_node_orchestrator import WorkflowOrchestrator

# Define project data
project_data = {
    "child_name": "أحمد",
    "child_age": 7,
    "child_gender": "male",
    "image_path": "/path/to/photo.jpg",
    "story_theme": "magical_adventure",
    "art_style": "pixar"
}

# Create orchestrator and execute workflow
orchestrator = WorkflowOrchestrator("My Project")
result = orchestrator.execute_workflow(project_data)

# Print results
print(result)
```

### Using the REST API

#### Start the API Server
```bash
python jomi_tomi_api_server.py
```

The API will be available at `http://localhost:5000`

#### Example API Requests

**Create a New Project:**
```bash
curl -X POST http://localhost:5000/api/v1/projects \
  -H "Content-Type: application/json" \
  -d '{
    "child_name": "أحمد",
    "child_age": 7,
    "child_gender": "male",
    "image_path": "/path/to/photo.jpg",
    "story_theme": "magical_adventure",
    "art_style": "pixar"
  }'
```

**Get Project Status:**
```bash
curl http://localhost:5000/api/v1/projects/<project_id>/status
```

**List All Projects:**
```bash
curl http://localhost:5000/api/v1/projects
```

**Get Available Art Styles:**
```bash
curl http://localhost:5000/api/v1/art-styles
```

---

## 📚 API Documentation

### Base URL
```
http://localhost:5000/api/v1
```

### Endpoints

#### 1. Health Check
- **Method:** GET
- **Path:** `/health`
- **Description:** Check if the API is running
- **Response:** `{ "status": "success", "service": "Jommi Tomi API Server" }`

#### 2. Create Project
- **Method:** POST
- **Path:** `/projects`
- **Description:** Create a new project and start the workflow
- **Request Body:**
  ```json
  {
    "child_name": "string",
    "child_age": "integer",
    "child_gender": "string (male/female/other)",
    "image_path": "string",
    "story_theme": "string",
    "art_style": "string (optional, default: pixar)"
  }
  ```
- **Response:** Project ID and execution summary

#### 3. List Projects
- **Method:** GET
- **Path:** `/projects`
- **Description:** Get all active projects
- **Response:** Array of projects with basic information

#### 4. Get Project Details
- **Method:** GET
- **Path:** `/projects/<project_id>`
- **Description:** Get detailed information about a specific project
- **Response:** Project data and execution results

#### 5. Get Project Status
- **Method:** GET
- **Path:** `/projects/<project_id>/status`
- **Description:** Get current status and progress of a project
- **Response:** Progress percentage and execution history

#### 6. Get Project Outputs
- **Method:** GET
- **Path:** `/projects/<project_id>/outputs`
- **Description:** Get all output files and artifacts
- **Response:** Paths to video, images, and social media content

#### 7. Get Art Styles
- **Method:** GET
- **Path:** `/art-styles`
- **Description:** Get list of available art styles
- **Response:** Array of art styles with descriptions

#### 8. Get Story Themes
- **Method:** GET
- **Path:** `/story-themes`
- **Description:** Get list of available story themes
- **Response:** Array of story themes with descriptions

---

## 📁 File Structure

```
jommi-tomi/
├── jomi_tomi_node_orchestrator.py    # Main orchestrator and node definitions
├── jomi_tomi_api_server.py           # Flask REST API server
├── jomi_tomi_technical_document.md   # Complete technical documentation
├── jomi_tomi_system_architecture.md  # System architecture details
├── jomi_tomi_prompt_library.md       # AI prompt library
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
└── config/
    └── prompts.json                  # Prompt configurations
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
FLASK_ENV=development
FLASK_DEBUG=True
API_PORT=5000
LOG_LEVEL=INFO
MAGNIFIC_API_KEY=your_api_key_here
ELEVENLABS_API_KEY=your_api_key_here
```

### Prompt Configuration

Edit `config/prompts.json` to customize prompts for different stages:

```json
{
  "character_generation": {
    "base_prompt": "A highly detailed, 3D rendered portrait...",
    "negative_prompt": "ugly, deformed, poorly drawn..."
  },
  "scene_generation": {
    "base_prompt": "A cinematic, wide-angle shot...",
    "negative_prompt": "ugly, deformed, poorly drawn..."
  }
}
```

---

## 🔧 Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
Follow PEP 8 guidelines. Use `black` for formatting:
```bash
black jomi_tomi_*.py
```

### Adding New Nodes
1. Create a new class inheriting from `Node`
2. Implement the `_process()` method
3. Register the node in `WorkflowOrchestrator._initialize_nodes()`

Example:
```python
class CustomNode(Node):
    def _process(self) -> Dict[str, Any]:
        # Your implementation here
        return {"result": "data"}
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📞 Support

For support, please contact:
- **Email:** support@jommi-tomi.com
- **Website:** https://jommi-tomi.com
- **Documentation:** https://docs.jommi-tomi.com

---

## 🙏 Acknowledgments

- Magnific.ai for image transformation capabilities
- Flask community for the excellent web framework
- All contributors and users of Jommi Tomi

---

**Version:** 1.0  
**Last Updated:** May 6, 2026  
**Author:** Manus AI
