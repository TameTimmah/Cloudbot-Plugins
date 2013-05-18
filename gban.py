from util import hook
 
 
@hook.command(adminonly=True)
def gban(inp, conn=None, chan=None, notice=None):
    "gline's <user> -- Makes the bot gline <user>. "
    user = inp.split(" ")[0]
    # You can use a regex to check if there are any characters in "user" here
    out = "gline %s" % (user)
    notice("Attempting to gline %s..." % (user))
    conn.send(out)