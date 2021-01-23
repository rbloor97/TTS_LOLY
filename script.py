import shlex, subprocess

lines = [line.rstrip('\n') for line in open('LPCNET/features.txt')]
print(lines)

count = 1

for line in lines:
    lpc_sintesis = './LPCNET/test_lpcnet ' + './LPCNET/' + line + ' ' + line+ '.s16'
    args = shlex.split(lpc_sintesis)
    subprocess.call(args)
    output = 'ffmpeg -f s16le -ar 16k -ac 1 -i ' + line +'.s16 audio' + str(count) + '-out.wav'
    args = shlex.split(output)
    print(output)
    subprocess.call(args)
    count +=1
