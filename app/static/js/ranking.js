
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


      function renderModal(data) {
        var extras = {}        
        var renderedPoints = ''
        var points_arr = []
        var th = []    
        var thArr = [] 
        var record = []   
        $(".label").tooltip({
          placement: "top"
        });
        
        
        $('.modal-title').text(data[0].records[0].name);

        
        $.each( data, function(i, records) {
                   
          
          $.each( records, function(i, record) {  
              
            $.each( record, function(i, items) {

              renderedPoints = ''
              var ordered = {};
                            
              $.each(items.points, function(i, points) {
                renderedPoints += '<span class="label label-success" data-show="tip" title="'+points.title+'">'+points.value+'</span>'+'<span class="label label-info" data-show="tip" title="Stig">'+points.points+'</span>';                
              })
       
              $('#profile > tbody').append(          
                '<tr>' + 
                  '<td>' + items.date + '</td>' +  
                  '<td>' + items.event + '</td>' +
                  '<td>' + items.category + '</td>' +
                  '<td>'+renderedPoints+'</td>' +
                  '<td>'+ items.total + '</td>' + 
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
              renderModal(data);
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

      $(".categories > li > a").click(function(e) {
        e.preventDefault();
        $('.categories > li').removeClass('active');
        $(e.target).parent().addClass('active');        
        getScore($(e.target).attr("href"));     
        return false;
      });
      
        $("body").tooltip({
          selector:'[data-show=tip]',
          "data-placement": "top",
        });

        getScore('/ranking/');
      