# Azure OpenAI Function Calling Demo

## Overview

This project demonstrates how Azure OpenAI GPT-4.1 can interact with external Python functions using Function Calling (Tool Calling).

Instead of answering everything from its own knowledge, the AI model can decide when additional information is required and request a specific function to retrieve that data.

In this example, the AI receives a weather-related question and automatically calls a Python function to obtain weather information for a city.

This is one of the core building blocks of Agentic AI systems.

---

## Objective

The goal of this project is to show how:

* Azure OpenAI GPT-4.1 can detect when a tool is needed.
* The model can request a function call.
* Python executes the requested function.
* External data can be returned to the application.
* AI and business logic can work together.

---

## How It Works

### Step 1: User Asks a Question

Example:

```text
Weather in Bangalore?
```

### Step 2: AI Analyzes the Request

The model receives:

* User question
* Available tools
* Tool descriptions
* Function parameters

The AI determines that weather information is needed.

---

### Step 3: AI Requests a Function Call

Instead of generating an answer directly, GPT-4.1 returns:

```json
{
  "name": "get_weather",
  "arguments": {
    "city": "Bangalore"
  }
}
```

This means:

* AI identified the correct tool.
* AI extracted the city name.
* AI prepared the required parameters.

---

### Step 4: Python Executes the Function

The application reads the tool call and executes:

```python
get_weather("Bangalore")
```

The function returns:

```text
Bangalore: 27°C, Cloudy
```

---

### Step 5: Application Receives Result

The result is returned to the Python application and can be:

* Displayed to users
* Stored in a database
* Sent back to GPT for final explanation
* Used by another system

---

## Architecture

```text
User
 │
 ▼
Weather in Bangalore?
 │
 ▼
Azure OpenAI GPT-4.1
 │
 ▼
Tool Decision
 │
 ▼
get_weather()
 │
 ▼
Python Function
 │
 ▼
Weather Result
 │
 ▼
Application Output
```

---

## Technologies Used

* Python
* Azure OpenAI
* GPT-4.1
* OpenAI SDK
* Function Calling
* JSON

---

## Key Concepts Demonstrated

### Function Calling

Allows AI models to invoke external functions when additional information is required.

### Tool Calling

Provides a controlled mechanism for AI to interact with external systems.

### Parameter Extraction

The model automatically extracts values such as:

```text
City = Bangalore
```

from natural language questions.

### Agentic AI Foundations

This project demonstrates the basic workflow used by AI Agents:

1. Understand request
2. Decide whether a tool is needed
3. Call tool
4. Receive result
5. Continue processing

---

## Current Implementation

The weather function currently returns mock data:

```python
def get_weather(city):
    return f"{city}: 27°C, Cloudy"
```

No external weather API is used.

---

## Future Enhancements

* OpenWeather API Integration
* Real-Time Weather Data
* Multiple Function Support
* Multi-Step Agent Workflows
* Database Queries
* ServiceNow Integration
* HCL Domino Monitoring Tools
* SQL Query Tools
* Enterprise Automation Agents

---

## Learning Outcome

After completing this project, developers will understand:

* Azure OpenAI Function Calling
* Tool Registration
* Tool Execution Flow
* AI-to-Python Communication
* Agentic AI Fundamentals
* Building Real-World AI Assistants

This project serves as a beginner-friendly introduction to Function Calling and Agentic AI using Azure OpenAI GPT-4.1.
