from fastmcp import FastMCP
mcp=FastMCP("calculator_server")
@mcp.tool()
def add(a:int,b:int)->int:
    "Add two number"
    return a+b
@mcp.tool()
def sub(a:int,b:int)->int:
    "Subtract two number"
    return a-b
@mcp.tool()
def mul(a:int,b:int)->int:
    "Multiply two number"
    return a*b
@mcp.tool()
def div(a:int,b:int)->float:
    "Divide two number"
    return a/b
@mcp.tool()
def mod(a:int,b:int)->int:
    "Modulus of two number"
    return a%b
# Run with HTTP transport
if __name__=="__main__": 
  mcp.run(transport="sse", host="0.0.0.0", port=8000)



