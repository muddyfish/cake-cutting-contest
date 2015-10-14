import json, random, copy, sys
import subprocess

MAX_DEGREES = 36000

f = open("answers.json")
answers = json.load(f)
f.close()

logfile = open("log.log", "a")
logfile.write("\n\nNEW RUN\n\n")

def get_botname(cmd): return cmd.split('"')[4].split(" ")[1]

def get_bot_bid(degrees_left, str_out):
    return min(degrees_left, max(0, int(float(str_out))))

def run_cmd(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).strip()
    except Exception as e:
        logfile.write("An Error occured running the bot: "+`cmd`+"\nException:\n"+`e`)
        return 0

def run_round(answers, max_degrees, degrees_left, max_people):
    bids = []
    for bot in answers:
        cmd = bot % (max_degrees, degrees_left, max_people, len(answers))
        print `cmd`,
        sys.stdout.flush()
        bids.append(get_bot_bid(degrees_left, run_cmd(cmd)))
        logfile.write(`cmd`+" bidded "+str(bids[-1])+"\n")
        print "bidded "+str(bids[-1])
    win = random.choice([i for i,bid in enumerate(bids) if bid == min(bids)])
    logfile.write("Bids: "+`bids` + " winning bid " + `bids[win]`+ "\n")
    degrees_left -= bids[win]
    bot = answers.pop(win)
    return degrees_left, answers, {get_botname(bot): bids[win]}

def run_cake(answers, max_degrees = 360):
    people = len(answers)
    max_people = people
    degrees_left = max_degrees
    bids = dict(zip(map(get_botname, answers), [0]*people))
    while people != 0 and degrees_left != 0:
        degrees_left, answers, tmp_dict = run_round(answers, max_degrees, degrees_left, max_people)
        bids.update(tmp_dict)
        people -= 1
        logfile.write("Degrees left: "+`degrees_left`+" Bots left: "+`map(get_botname, answers)`+"\n")
    print degrees_left
    return bids

#for i in range(1):
while 1:
    logfile.write("\n\nNEW ROUND\n\n")
    bids = run_cake(copy.deepcopy(answers), MAX_DEGREES)
    for bid in sorted(bids.iteritems(), key = lambda x: -x[1]): print "%r: %r"%(bid)
    logfile.write("\n"+json.dumps(bids)+"\n")
    logfile.flush()
