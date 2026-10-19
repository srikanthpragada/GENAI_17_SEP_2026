from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("File Server")


# Load contents of the file
@mcp.tool()
def read_file(filename: str) -> str:
    """Reads the contents of the given file and return contents
       Return empty string on error
    """
    try:
        with open(filename, "rt") as f:
            return f.read()
    except:
        print(f"Sorry! Could not read file {filename}")
        return "" 


mcp.run(transport="http", port = 9000)
