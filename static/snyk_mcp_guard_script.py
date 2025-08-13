import json
import os


def create_rules():
    print("Creating rules...")
    # Create the .cursor/rules directory if it doesn't exist
    cursor_rules_path = ".cursor/rules"
    if not os.path.exists(cursor_rules_path):
        os.makedirs(cursor_rules_path)

    # Write the SAST rule file
    sast_rule_path = os.path.join(cursor_rules_path, "01-SAST_scan.mdc")
    sast_rule_content = "\n".join([
        "---",
        "description: Run Snyk Code",
        "globs:",
        "alwaysApply: always",
        "---\n",
        "- Always run Snyk Code scanning tool for new first party code generated.\n"
    ])
    with open(sast_rule_path, "w") as f:
        f.write(sast_rule_content)

    # Write the SCA rule file
    sca_rule_path = os.path.join(cursor_rules_path, "02-SCA_scan.mdc")
    sca_rule_content = "\n".join([
        "---",
        "description: Run Snyk Open Source",
        "globs:",
        "alwaysApply: always",
        "---\n",
        "- Always run Snyk SCA scanning tool for new dependencies or dependency updates.\n"
    ])
        
    with open(sca_rule_path, "w") as f:
        f.write(sca_rule_content)

    print("Rules created successfully.")

def add_snyk_mcp_config(file_path=".cursor/mcp.json"):
    """
    Adds the Snyk MCP configuration to a given JSON file.

    Args:
        file_path (str): The path to the configuration file.
                         Defaults to "mcp-config.json" in the current directory.
    """
    snyk_mcp_config = {
        "snyk": {
            "command": "npx",
            "args": ["-y", "snyk@latest", "mcp", "-t", "stdio"],
            "env": {}
        }
    }

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Creating a new mcp file.")
        existing_data = {"mcpServers": {}}
        # If the file does not exist, create it with an empty JSON object
        # and ensure the parent directory exists.
        parent_dir = os.path.dirname(os.path.expanduser(file_path))
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)
        with open(os.path.expanduser(file_path), "w") as f:
            json.dump({"mcpServers": {}}, f, indent=4)
        existing_data = {"mcpServers": {}}
    else:
        try:
            with open(file_path, 'r') as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {file_path}. Starting with a new config.")
            existing_data = {"mcpServers": {}}
    
    # Ensure the 'mcpServers' key exists
    if "mcpServers" not in existing_data:
        existing_data["mcpServers"] = {}

    # Update the mcpServers with the Snyk configuration
    existing_data["mcpServers"].update(snyk_mcp_config)

    # Write the updated configuration back to the file
    try:
        with open(file_path, 'w') as f:
            json.dump(existing_data, f, indent=4)
        print(f"Successfully added Snyk MCP configuration to {file_path}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

    

# Example usage:
if __name__ == "__main__":
    add_snyk_mcp_config()
    create_rules()
