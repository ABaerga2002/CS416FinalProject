function addToCart(url){
     $.ajax({
            url: url,
            method: 'GET',
            success: function(response) {
                alert(response.message);
            },
            error: function(xhr, status, error) {
                alert('Error adding event to cart');
            }
        });
}

function deleteItem(url, eventID){
     $.ajax({
            url: url,
            method: 'GET',
            success: function(response) {
                if(response.deleted){
                    $('#event-' + eventID).remove();
                }
                alert(response.message);
            },
            error: function(xhr, status, error) {
                alert('Error removing event to cart');
            }
        });
}