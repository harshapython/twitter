function toggleFollow(x)
   {
        $.ajax({
            url: "{% url 'profile' pk=1 %}",
            data: {
              'action': 'follow'
              'id': x
            },
            dataType: 'json',
            success: function () {
                console.log(success) 
                $("#follow_btn").hide();
                $("#unfollow_btn").show();

            }
        });        
    }
    function x()
    {

    }