var mysql = require('mysql');
// Create connection to data base
var con = mysql.createConnection({
    host: "webdb.uvm.edu",
    user: "mgreen13_admin",
    password: "7oGdoDnzJ9IK8nS8",
    database: "MGREEN13_moonboard"
})


// create table 
con.connect(function(err) {
    if (err) throw err;
    console.log("con!");
    var sql = "CREATE TABLE hold_type (one INT, two INT, three INT, four INT, five INT, six INT, seven INT, eight INT, nine INT, ten INT, eleven INT, twelve INT, thirteen INT, fourteen INT, fifteen INT, sixteen INT, seventeen INT, eighteen INT, nineteen INT, twenty INT, twenty_one INT, twenty_two INT, twenty_three INT, twenty_four INT, twenty_five INT, twenty_six INT, twenty_seven INT, twenty_eight INT, twenty_nine INT, thirty INT, thirty_one INT, thirty_two INT, thirty_three INT, thirty_four INT, thirty_five INT, thirty_six INT, thirty_seven INT, thirty_eight INT, thirty_nine INT, forty INT, fifty INT, fifty_one INT, fifty_two INT, fifty_three INT, fifty_four INT, fifty_five INT, fifty_six INT, fifty_seven INT, fifty_eight INT, fifty_nine INT, sixty INT, sixty_one INT, sixty_two INT, sixty_three INT, sixty_four INT, sixty_five INT, sixty_six INT, sixty_seven INT, sixty_eight INT, sixty_nine INT, seventy INT, seventy_one INT, seventy_two INT, seventy_three INT, seventy_four INT, seventy_five INT, seventy_six INT, seventy_seven INT, seventy_eight INT, seventy_nine INT, eighty INT, eighty_one INT, eighty_two INT, eighty_three INT, eighty_four INT, eighty_five INT, eighty_six INT, eighty_seven INT, eighty_eight INT, eighty_nine INT, ninety INT, ninety_one INT, ninety_two INT, ninety_three INT, ninety_four INT, ninety_five INT, ninety_six INT, ninety_seven INT, ninety_eight INT, ninety_nine INT, one_hundred INT, one_hundred_and_one INT, one_hundred_and_two INT, one_hundred_and_three INT, one_hundred_and_four INT, one_hundred_and_five INT, one_hundred_and_six INT, one_hundred_and_seven INT, one_hundred_and_eight INT, one_hundred_and_nine INT, one_hundred_and_ten INT, one_hundred_and_eleven INT, one_hundred_and_twelve INT, one_hundred_and_thirteen INT, one_hundred_and_fourteen INT, one_hundred_and_fifteen INT, one_hundred_and_sixteen INT, one_hundred_and_seventeen INT, one_hundred_and_eighteen INT, one_hundred_and_nineteen INT, one_hundred_and_twenty INT, one_hundred_and_twenty_one INT, one_hundred_and_twenty_two INT, one_hundred_and_twenty_three INT, one_hundred_and_twenty_four INT, one_hundred_and_twenty_five INT, one_hundred_and_twenty_six INT, one_hundred_and_twenty_seven INT, one_hundred_and_twenty_eight INT, one_hundred_and_twenty_nine INT, one_hundred_and_thirty INT, one_hundred_and_thirty_one INT, one_hundred_and_thirty_two INT, one_hundred_and_thirty_three INT, one_hundred_and_thirty_four INT, one_hundred_and_thirty_five INT, one_hundred_and_thirty_six INT, one_hundred_and_thirty_seven INT, one_hundred_and_thirty_eight INT, one_hundred_and_thirty_nine INT, one_hundred_and_forty INT, one_hundred_and_forty_one INT, one_hundred_and_forty_two INT, one_hundred_and_forty_three INT, one_hundred_and_forty_four INT, one_hundred_and_forty_five INT, one_hundred_and_forty_six INT, one_hundred_and_forty_seven INT, one_hundred_and_forty_eight INT, one_hundred_and_forty_nine INT, one_hundred_and_fifty INT)";
    con.query(sql, function(err, result) {
    if (err) throw err;
        console.log("Table created");
    });
});
