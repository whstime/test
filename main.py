from pyodide import create_proxy
console.log("starting")
toggleButton = document.getElementById('toggle')
def toggleBorders(event):
 global isBorderToggled
 console.log("toggled")
 if isBorderToggled == False: 
  isBorderToggled = True
  for x in document.getElementsByClassName("command"):
   x.style.border = "1px solid white"
 else:
  isBorderToggled = False
  for x in document.getElementsByClassName("command"):
   x.style.border = "none"
#  for x in document.getElementsByClassName("command"):
#   if borders == False:
#     x.style.border = "1px solid white"
#     borders = True
#   else:
#     x.style.border = "none"
#     borders = False
tb = create_proxy(toggleBorders)
toggleButton.addEventListener("click",tb)
isBorderToggled = False