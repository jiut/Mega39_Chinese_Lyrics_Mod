middleStr = '78\na\nv\nv\nvariousvafsd\nsdsd';
lines = middleStr.split('\n');

for (let index = 1; index < lines.length; index++) {
    if (lines[0] > 0 && lines[0] < 1000) {
        var number = lines[0].padStart(3,'0');
    }
    let start = (index).toString().padStart(3,'0');
    lines[index] = 'pv_' + number + '.lyric.' + start+ '=' + lines[index];
}
return lines.join('\n');