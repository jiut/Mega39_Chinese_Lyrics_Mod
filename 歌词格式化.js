lines = middleStr.split('\n');

var number;

if( isNaN(parseInt(lines[0]) ) ){
    number = parseInt(lines[ lines.length - 1 ]);
    lines.pop();
}
else{
    number = parseInt(lines[0]);
    lines.shift();
}

if (number > 0 && number < 1000) {
        number = number.toString().padStart(3, '0');
}

for (let index = 0; index < lines.length; index++) {
    let start = (index+1).toString().padStart(3,'0');
    lines[index] = 'pv_' + number + '.lyric.' + start+ '=' + lines[index];
}

output = lines.join('\n').trim();

return output;