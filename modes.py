# Plugin made by TameTimmah
# Has Modes
# Owner, SuperOP, OP, HalfOP, Voice, Ban, KBan
# All with Reverse Added e.g DeOp

from util import hook

@hook.command(adminonly=True)
def owner(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s +q %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s +q %s" % (chan, user)
    notice("Attempting to Owner %s on %s..." % (user, chan))
    conn.send(out)


@hook.command(adminonly=True)
def superop(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s +a %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s +a %s" % (chan, user)
    notice("Attempting to SuperOP %s on %s..." % (user, chan))
    conn.send(out)
	
	
@hook.command(adminonly=True)
def op(inp, conn=None, chan=None, notice=None):
    "op [channel] <user> -- OP's the <user> in [channel]. "\
    "If [channel] is left blank the bot will OP in "\
    "the channel it was sent"
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s +o %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s +o %s" % (chan, user)
    notice("Attempting to OP %s on %s..." % (user, chan))
    conn.send(out)
	
	
@hook.command(adminonly=True)
def halfop(inp, conn=None, chan=None, notice=None):
    "halfop [channel] <user> -- HalfOp's the <user> in [channel]. "\
    "If [channel] is left blank the bot will HalfOp in "\
    "the channel it was sent"
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s +h %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s +h %s" % (chan, user)
    notice("Attempting to HalfOP %s on %s..." % (user, chan))
    conn.send(out)
	
	
@hook.command(adminonly=True)
def voice(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s +v %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s +v %s" % (chan, user)
    notice("Attempting to Voice %s on %s..." % (user, chan))
    conn.send(out)
	
	
@hook.command(adminonly=True)
def ban(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s +b %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s +b %s" % (chan, user)
    notice("Attempting to Ban %s from %s..." % (user, chan))
    conn.send(out)
	
@hook.command(adminonly=True)
def kban(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out1 = "MODE %s +b %s" % (chan, user)
        out2 = "KICK %s %s" % (chan, user)
        if len(inp) > 2:
            reason = ""
            for x in inp[2:]:
                reason = reason + x + " "
            reason = reason[:-1]
            out = out + " :" + reason
    else:
        user = inp[0]
        out1 = "MODE %s +b %s" % (chan, user)
        out2 = "KICK %s %s" % (chan, user)
        if len(inp) > 1:
            reason = ""
            for x in inp[1:]:
                reason = reason + x + " "
            reason = reason[:-1]
            out = out + " :" + reason

    notice("Attempting to kickban %s from %s..." % (user, chan))
    conn.send(out1)
    conn.send(out2)


@hook.command(adminonly=True)
def deowner(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s -q %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s -q %s" % (chan, user)
    notice("Attempting to DeOwner %s on %s..." % (user, chan))
    conn.send(out)
	
	
@hook.command(adminonly=True)
def desuperop(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s -a %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s -a %s" % (chan, user)
    notice("Attempting to DeSuperOp %s on %s..." % (user, chan))
    conn.send(out)
	
	
@hook.command(adminonly=True)
def deop(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s -o %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s -o %s" % (chan, user)
    notice("Attempting to DeOP %s on %s..." % (user, chan))
    conn.send(out)
	
	
@hook.command(adminonly=True)
def dehalfop(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s -h %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s -h %s" % (chan, user)
    notice("Attempting to DeHalfOp %s on %s..." % (user, chan))
    conn.send(out)
	
@hook.command(adminonly=True)
def devoice(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s -v %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s -v %s" % (chan, user)
    notice("Attempting to DeVoice %s on %s..." % (user, chan))
    conn.send(out)
	
	
@hook.command(adminonly=True)
def unban(inp, conn=None, chan=None, notice=None):
    inp = inp.split(" ")
    if inp[0][0] == "#":
        chan = inp[0]
        user = inp[1]
        out = "MODE %s -b %s" % (chan, user)
    else:
        user = inp[0]
        out = "MODE %s -b %s" % (chan, user)
    notice("Attempting to Unban %s from %s..." % (user, chan))
    conn.send(out)