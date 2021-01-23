import shlex, subprocess


sintesis = 'python synthesize.py --model="Tacotron"'
args = shlex.split(sintesis)
#subprocess.call(args)

#print(command_line)

features = 'mv *.f32 LPCNET && ls LPCNET/*.f32 | cat > features.txt'
args = shlex.split(features)
#subprocess.call(args)


lines = [line.rstrip('\n') for line in open('LPCNET/features.txt')]
print(lines)

count = 1
for line in lines:
    lpc_sintesis = './LPCNET/test_lpcnet ' + line + ' ' + line+ '.s16'
    args = shlex.split(lpc_sintesis)
    output = 'ffmpeg -f s16le -ar 16k -ac 1 -i ' + line +'.s16 ../audio' + str(count) + '-out.wav'
    args = shlex.split(output)
    print(output)
    #subprocess.call(args)
    count +=1





