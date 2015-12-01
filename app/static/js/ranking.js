
      function getScore (url) {
        $('#ranking > tbody').empty();
        $.ajax({
            url: url,
            type: 'GET',
            success: function(data){ 
              data.sort(orderPoints);

              $.each( data, function( key, value ) {
                $('#ranking > tbody').append(          
                  '<tr>' + 
                    '<td id="rank">' + (key+1) + '</td>' +  
                    '<td id="name"><a href="/ranking/athlete/'+value.id+'/">' + value.name + '</a>' + '</td>' +
                    '<td id="points">'+value.points + '</td>' +
                  '</tr>');
                
              });
            },
            error: function(data) {
                console.log(data); //or whatever
            }
        });        
      };

      function renderData(data) {
        $('.modal-title').text(data[0].record[0].name);
        $.each( data, function(i, record) {              
          $.each( record, function(x, item) {
            $.each(item, function(key, value) {
              $('#profile > tbody').append(          
                '<tr>' + 
                  '<td>' + value.date + '</td>' +  
                  '<td>' + value.tournament + '</td>' +
                  '<td>' + value.category + '</td>' +
                  '<td>'+ value.place + '</td>' +
                  '<td>'+ value.points + '</td>' +
                '</tr>');
              
            });
          });
        });

        $('#myModal').modal();
      };

      function getAthlete (url) { 
        $('#profile > tbody').empty();     
        $.ajax({
            url: url,
            type: 'GET',
            success: function(data){               
              renderData(data);
            },
            error: function(data) {
                console.log(data); //or whatever
            }
        });        
      };

      function orderPoints(a,b) {
        return parseInt(b.points, 10) - parseInt(a.points, 10);
      };

      $(document).on('click','#name > a',function(e){

        e.preventDefault();
        getAthlete($(e.target).attr("href"));     
        return false;
      });

      $("#total").click(function(event) {
        event.preventDefault();
        $('li').removeClass('active');
        $("#total").parent().addClass('active');    
        getScore($("#total").attr('href'));
      });

      $("#sparring").click(function(event) {
        event.preventDefault();
        $('li').removeClass('active');
        $("#sparring").parent().addClass('active');
        getScore($("#sparring").attr('href'));
      });

      $("#poomsae").click(function(event) {
        event.preventDefault();
        $('li').removeClass('active');
        $("#poomsae").parent().addClass('active');
        getScore($("#poomsae").attr('href'));
      });


        
        getScore('/ranking/');
      