$.ajax({
type: 'POST',
data: {Power: 0},
dataType: "text",
success: function(data){
            alert("PC Powered Down");
            }
});
