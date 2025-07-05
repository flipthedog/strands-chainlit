# Strands + Chainlit Integration Demo

A demonstration project showcasing the integration between [Strands](https://github.com/pipecat-ai/strands) AI agents and [Chainlit](https://chainlit.io/) for building interactive chat applications.

This project demonstrates how to:
- Create an AI agent using the Strands framework with AWS Bedrock
- Build a web-based chat interface using Chainlit
- Stream responses from the agent to provide real-time conversation
- Integrate tools (like a calculator) into the agent

## Features

- **Strands Agent**: Uses Amazon Nova Lite model via AWS Bedrock
- **Tool Integration**: Built-in calculator tool for mathematical operations
- **Streaming Responses**: Real-time message streaming for better user experience
- **Web Interface**: Clean, modern chat interface powered by Chainlit
- **Session Management**: Maintains conversation history per user session

## Prerequisites

Before setting up this project, ensure you have:

1. **Python 3.13+** installed
2. **UV package manager** ([installation guide](https://docs.astral.sh/uv/getting-started/installation/))
3. **AWS Credentials** configured for Bedrock access:
   - AWS CLI configured with `aws configure`
   - Or environment variables: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`
   - Ensure your AWS account has access to Amazon Bedrock and the Nova Lite model

## Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd strands-chainlit
   ```

2. **Install dependencies** using UV:
   ```bash
   uv install
   ```

3. **Verify AWS credentials** are configured:
   ```bash
   aws sts get-caller-identity
   ```

## Usage

### Running the Application

Start the Chainlit server:

```bash
chainlit run app.py
```

The application will be available at `http://localhost:8000` by default.

### Using the Chat Interface

1. Open your browser and navigate to the application URL
2. Start a conversation by typing a message
3. The agent can:
   - Answer general questions
   - Perform calculations using the built-in calculator tool
   - Maintain conversation context throughout the session

### Example Interactions

**Basic conversation:**
```
User: Hello! How are you today?
Agent: Hello! I'm doing well, thank you for asking. I'm here to help you with any questions or tasks you might have. How can I assist you today?
```

**Using the calculator tool:**
```
User: What's 25 * 42 + 17?
Agent: I'll calculate that for you using the calculator tool.
[Agent uses calculator tool]
The result is 1067.
```

## Project Structure

```
strands-chainlit/
├── app.py              # Main Chainlit application
├── agent.py            # Strands agent configuration
├── chainlit.md         # Welcome screen content
├── pyproject.toml      # Project dependencies
├── README.md           # This file
└── uv.lock            # Dependency lock file
```

### Key Components

- **`app.py`**: Contains the Chainlit application setup with message handlers
- **`agent.py`**: Defines the `DemoAgent` class that wraps the Strands agent
- **`chainlit.md`**: Welcome screen content displayed when users first visit

## Configuration

### AWS Bedrock Model

The agent is configured to use Amazon Nova Lite (`us.amazon.nova-lite-v1:0`) in the `us-east-2` region. To modify this:

1. Edit `agent.py`
2. Change the `model_id` and `region_name` in the `BedrockModel` initialization:

```python
self.model = BedrockModel(
    model_id="your-preferred-model-id", 
    region_name="your-preferred-region"
)
```

### Adding More Tools

To add additional tools to the agent:

1. Import the desired tools from `strands_tools`
2. Add them to the `tools` list in `agent.py`:

```python
from strands_tools import calculator, web_search, file_reader

# In DemoAgent.__init__():
self.agent = Agent(
    model=self.model, 
    tools=[calculator, web_search, file_reader],
    callback_handler=None
)
```

## Development

### Running in Development Mode

For development with auto-reload:

```bash
chainlit run app.py --watch
```

### Debugging

Enable debug logging by setting the environment variable:

```bash
export CHAINLIT_DEBUG=true
chainlit run app.py
```

## Troubleshooting

### Common Issues

1. **AWS Credentials Error**:
   - Ensure AWS credentials are properly configured
   - Check that your AWS account has Bedrock access
   - Verify the model is available in your selected region

2. **Import Errors**:
   - Run `uv install` to ensure all dependencies are installed
   - Check that you're using Python 3.13+

3. **Port Already in Use**:
   - Change the port with: `chainlit run app.py --port 8001`

### Getting Help

- **Chainlit Documentation**: https://docs.chainlit.io
- **Strands Documentation**: Check the Strands repository
- **AWS Bedrock Documentation**: https://docs.aws.amazon.com/bedrock/

## License

[Specify your license here]

## Contributing

[Add contribution guidelines if applicable]
