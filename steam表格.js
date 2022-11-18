var lines = middleStr.split('\n');
let i = 0;
while(i < lines.length){
    lines[i] = lines[i].trim().replaceAll('\n', '');
    i++;
}

output = '';

for (i = 0; i < lines.length; i++) {
    if (lines[i] !== '') {
        if (i === 0 || lines[i-1] === '') {
            output += "[tr]\n";
        }

        output += "    [td]" + lines[i] + "[/td]\n";

        if( i === lines.length - 1 || lines[i+1] === '' ){
            output += "[/tr]\n";
        }
    }
}

return output;