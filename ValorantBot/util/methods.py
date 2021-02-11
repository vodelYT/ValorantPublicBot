import numpy
from discord.utils import get
from ValorantBot.util import sql

valid_roles = numpy.array(["Iron 1", "Iron 2", "Iron 3",
                           "Bronze 1", "Bronze 2", "Bronze 3",
                           "Silver 1", "Silver 2", "Silver 3",
                           "Gold 1", "Gold 2", "Gold 3",
                           "Platinum 1", "Platinum 2", "Platinum 3",
                           "Diamond 1", "Diamond 2", "Diamond 3",
                           "Immortal",
                           "Radiant",
                           ])

unvalid_roles = ["Administrator", "Moderator"]


async def get_rank(dcUser):
    roles_ROLES = dcUser.roles
    roles_NAME = []
    for roles_ROLE in roles_ROLES:
        roles_NAME += [roles_ROLE.name]

    roles_NAME_filtered = numpy.setdiff1d(roles_NAME, unvalid_roles)
    roles_NAME_filtered = roles_NAME_filtered.tolist()
    roles_NAME_filtered.remove("@everyone")

    role = get(dcUser.guild.roles, name=roles_NAME_filtered[0])

    return role


async def set_rank(ctx, dcUser, rank):
    old_roles_ROLES = dcUser.roles
    old_roles_NAME = []
    for old_roles_ROLE in old_roles_ROLES:
        old_roles_NAME += [old_roles_ROLE.name]

    old_roles_NAME_filtered = numpy.setdiff1d(old_roles_NAME, valid_roles)
    old_roles_NAME_filtered = old_roles_NAME_filtered.tolist()
    old_roles_NAME_filtered.remove("@everyone")

    await dcUser.edit(roles=[])
    await dcUser.add_roles(rank)

    sql.update_rank(dcUser.id, rank)

    for i in old_roles_NAME_filtered:
        await dcUser.add_roles(get(dcUser.guild.roles, name=i))

# async def check_profile(bot, vclient):
#   guild_members = bot.guilds[0].members
#   for member in guild_members:
#     if await get_rank(member) != None:
#       if member.nick != None:
#         if not member.bot:
#           nickname = member.nick
#           x = nickname.split('#')
#           print(x)
#           dcName = x[0]
#           dcTag = x[1]


#           if sql.user_exists(member.id):
#             valPUUID = sql.get_puuid(member.id)

#             valUser = vclient.get_user(valPUUID, "puuid")
#             valTag = valUser.__getattribute__("tagLine")
#             valName = valUser.__getattribute__("gameName")

#             if dcTag != valTag:
#               sql.update_tag(member.id, valTag)
#               try:
#                 await member.edit(nick=valName+"#"+valTag)
#               except:
#                 print("error updating user tag")
#             elif dcName != valName:
#               sql.update_name(member.id, valName) 
#               try:
#                 await member.edit(nick=valName+"#"+valTag)
#               except:
#                 print("error updating user name")
