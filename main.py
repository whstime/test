from pyodide import create_proxy
console.log("starting")
toggleButton = document.getElementById('toggle')
isBorderToggled = False
def toggleBorders(event):
 nonlocal isBorderToggled
 console.log("toggled")
 console.log("Variable isBorderToggled:", isBorderToggled)
 if isBorderToggled == False: 
  isBorderToggled = True
  for x in document.getElementsByClassName("command"):
   x.style.border = "1px solid white"
 else:
  isBorderToggled = False
  for x in document.getElementsByClassName("command"):
   x.style.border = "none"
tb = create_proxy(toggleBorders)
toggleButton.addEventListener("click",tb)
