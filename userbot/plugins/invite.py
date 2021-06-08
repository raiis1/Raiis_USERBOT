#ZedThon



from telethon import functions


@icssbot.on(admin_cmd(pattern="اضف ?(.*)"))
@icssbot.on(sudo_cmd(pattern="اضف ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await edit_delete(
            event, "⌔∮ `.اضف` المستخدمين الى كروب ، ليس لمراسلته في الخاص", 5
        )
    else:
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await event.client(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await edit_delete(event, f"⌔∮ `{str(e)}`", 5)
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await event.client(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    await edit_delete(event, f"`{str(e)}`", 5)

        await edit_or_reply(event, f"**⌔∮** `{to_add_users}` **هو بالـفعل مضاف.** ")


CMD_HELP.update(
    {
        "invite": """**Plugin : **`invite`

  •  **Syntax : **`.اضف معرف(s)/او ايدي المستخدم(s)`
  •  **Function : **__Add the given user/users to the group where u used the command__
"""
    }
)
