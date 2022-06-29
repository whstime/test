from pyodide import create_proxy
console.log("starting")
def toggleBorders(event):
 console.log("toggled")
 for x in document.getElementsByClassName("command"):
    if x.style.outline == "none":
     x.style.outline = "1px solid white"
    else:
     x.style.outline = "none"
toggleButton = document.getElementById('toggle')
tb = create_proxy(toggleBorders)
toggleButton.addEventListener("click",tb)
