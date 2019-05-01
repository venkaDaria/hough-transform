jQuery(function($) {
    $('#source').on('change', function() {
        $("#images").prop('disabled', this.value != "own")
        $("#dataset").prop('disabled', this.value == "own")
    });
})

$('#myCarousel').carousel({});

function save_dataset(data) {
    $.post("/api/save", {'data': data}, function(data) {
        console.log("Data are saved in the result folder")
    });
}

function clear_result() {
    $.post( "/api/clear", function(data) {
        document.location.href = "/"
    });
}

function set_label(input) {
    var names = ""
    for (var i = 0; i < input.files.length; i++) {
        names += input.files[i].name
        if (i < input.files.length - 1) {
            names += ", "
        }
    }
    $("#images_label").text(names)
}

var start_active = '<div class="carousel-item row no-gutters active">'
var start = '<div class="carousel-item row no-gutters">'
var end = '</div>'

function get_main(data) {
    return '<div class="col-3 float-left"><img class="img-fluid" src="' + data + '"></div>'
}

function get_value(data) {
    return '<input name="images_data" value="' + data + '" type="hidden"/>';
}

function get_start(count, max) {
    return count == 3 || count + 1 == max ?  start_active : start
}

function readURL(input) {
    set_label(input)
    $("#images_data").html('')

    if (input.files && input.files[0]) {
        var count = 0
        $("#main_dataset").html('')
        var partHtml = ""

        for (var i = 0; i < input.files.length; i++) {
            var reader = new FileReader()

            reader.onload = function(e) {
                $("#images_data").append(get_value(e.target.result))

                partHtml += get_main(e.target.result)

                if ((count + 1) % 4 == 0 || count + 1 == input.files.length) {
                    partHtml = get_start(count, input.files.length) + partHtml + end
                    $("#main_dataset").append(partHtml)
                    partHtml = ""
                }

                count++
            }

            reader.readAsDataURL(input.files[i])
        }
    }
}
