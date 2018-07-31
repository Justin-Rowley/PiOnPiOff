$.ajax({
type: 'POST',
data: {Power: 1},
dataType: "text",
success: function(data){
            alert("PC Powered On");
            }
});
