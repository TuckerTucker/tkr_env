# Basic Python Virtual Envirionment Set Up

 Automatically sets up a Python virtual environment, checks the availability of a local LM Studio server, and falls back to OpenAI's API if the local server is not available. The project includes scripts for environment setup and server interaction, making it easy to start experimenting with LLMs.


## What it does

Run the script

    ```bash
    ./tkr_env.sh
    ```
    or 

    ```bash
    source tkr_env.sh
    ```

1. First it checks if the environment exists.
No environment? - Creates and activates the environtment then installs all packages in 'requirements' (listed below). 
Environment? - Activates the environment.

then runs Welcome.py

2. **Check LLM Servers'**: The `welcome.py` script is executed automatically after the environment setup.
It checks for the availability of the local LLM server. 

LM Studio server active? - It'll use that. 
Not active? - Uses OpenAI (ensure you have a valid api key in your .env file)

Create a .env 
add your api key without quotes.

``` .env
OPENAI_API_KEY=sk-123456789
```

3. **When you're done**
You can deactivate the virtual environment by running:

    ```bash
    deactivate
    ```

### Change Environment Nmme
Set the `env_name` variable in `tkr_env.sh` to customize the name of the virtual environment before it's created.
*To change the environment name after it's created you'll need to do it manually.*