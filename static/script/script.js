let textbox = document.getElementById("message")
        
let timer = setTimeout(function() {
        location.reload();
    }, 5000)
                
textbox.onkeydown = function(e) {            
            
    clearTimeout(timer)
                    
    timer = setTimeout(function() {
        location.reload();
    }, 5000)
}    