env_name="project_env"

# Check if the virtual environment already exists
if [ -d "$env_name" ]; then
    source "$env_name/bin/activate"
    echo -e "\e[38;5;208mActivated '$env_name'.\e[0m"
    
else
    # Create the virtual environment if it does not exist
    python3 -m venv $env_name
    echo -e "\e[38;5;208mCreated '$env_name'.\e[0m"
    # Define a timeout in seconds and polling interval (e.g., half a second)
    timeout=30
    elapsed=0
    poll_interval=0.5
    pip_interval=1

    # Check if the activation script exists, with polling
    while [ $elapsed -lt $timeout ]; do
        if [ -f "$env_name/bin/activate" ]; then
            source "$env_name/bin/activate"
            echo -e "\e[38;5;208mActivated '$env_name'.\e[0m"
            # Check if the virtual environment is correctly activated
            if [[ -z "$VIRTUAL_ENV" ]]; then
                echo -e "\e[38;5;201mThe virtual environment is not activated properly. Please check the environment.\e[0m"
                break
            else
                echo -e "\e[38;5;208mInstalling requirements with pip \e[0m"
                pip install -r requirements -q > /dev/null 2>&1 &
                
                while kill -0 $! 2> /dev/null; do
                    echo -n '. '
                    sleep $pip_interval
                done
                echo "\n"
            fi
            break
        else
            echo -e "\e[38;5;208mWaiting for the virtual environment to be ready...\e[0m"
            sleep $poll_interval
            elapsed=$(echo "$elapsed + $poll_interval" | bc)
        fi
    done
fi

# Check if we reached the timeout without activating the environment
if (( $(echo "$elapsed >= $timeout" | bc -l) )); then
    echo -e "\e[38;5;201mFailed to create or activate virtual environment within the expected time.\e[0m"
fi

python welcome.py
