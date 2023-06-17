import disnake
from disnake.ext import commands


class FUDSTOPMenu(disnake.ui.Select):
    def __init__(self):

        options = [
    
            disnake.SelectOption(label="map🗾Heatmaps"),
            disnake.SelectOption(label="ch💬Chats⬅"),
            disnake.SelectOption(label="flow💦Options Flow"),
            disnake.SelectOption(label="fd📶Market & Social Feeds"),
            disnake.SelectOption(label="rss🔊RSS Feeds"),
            disnake.SelectOption(label="nw🌐News Feeds"),
            disnake.SelectOption(label="tt🚀TradyTics Realtime Alerts"),
            disnake.SelectOption(label="fm📜Forums"),
            disnake.SelectOption(label="ut💡Utilities Sector"),
            disnake.SelectOption(label="etf⚓ETF Sector"),
            disnake.SelectOption(label="cc🌒Consumer Cyclical Sector"),
            disnake.SelectOption(label="cs📣Communication Services Sector"),
            disnake.SelectOption(label="re🏠Real Estate Sector"),
            disnake.SelectOption(label="he💉Healthcare Sector"),
            disnake.SelectOption(label="te💿Technology Sector"),
            disnake.SelectOption(label="in🌆Industrials Sector"),
            disnake.SelectOption(label="cd⛴️Consumer Defensive Sector"),
            disnake.SelectOption(label="fs💰Financial Services Sector"),
            disnake.SelectOption(label="en⚡Energy Sector"),
            disnake.SelectOption(label="bm🧱Basic Materials Sector")]

        super().__init__(
            placeholder="🇫 🇺 🇩 🇸 🇹 🇴 🇵 ☯️ 🇲 🇪 🇳 🇺",
            min_values=1,
            max_values=1,
            custom_id="selec_menu:FUDSTOPMenu",
            options=options
        )

    async def callback(self, interaction:disnake.MessageCommandInteraction):
        await interaction.response.defer(with_message=True, ephemeral=True)
        em = disnake.Embed(title=f"Welcome to FUDSTOP", description="```py\nThis is the server Menu. For those that are new - it's a great place to start going through the channels and begin customizing your notifications.\n\nWe offer over 175 channels with a plethora of tools, resources, and feeds that you can have streamlined to your PC or mobile device. Select from the menu below to get started!\n\n\nWhen you select from the menu - the command /navigate will be printed alongside the key to type into the search box. Simply click the command and type in the key to being findind what you need!``` ```py\nNote: The messages will dissapear after 30 seconds.```", color=disnake.Colour.dark_gold())
        if self.values[0] == "map🗾Heatmaps":
            em2 = disnake.Embed(title="map🗾Heatmaps", description=f"```py\nThis section provides automated heatmaps covering six different market indexes.``` ```py\nKeycode: map```",color=disnake.Colour.dark_green())
            em2.add_field(name="🗾",value="<#1035270377414336662>")
            em2.add_field(name="🗾",value="<#1035270668901699584>")
            em2.add_field(name="🗾",value="<#1035270694990262302>")
            em2.add_field(name="🗾",value="<#1035270719338201088>")
            em2.add_field(name="🗾",value="<#1035270806479056946>")
            em2.add_field(name="🗾",value="<#1035270870320562267>")
            em2.add_field(name="🗾",value="<#1035270941208498186>")
            em2.add_field(name="Navigation Code:",value="```py\nmap```")
            em2.set_footer(text="`All map channels provide the heat-map for the specific index.`")
            await interaction.edit_original_message(embed=em2)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)





        elif self.values[0] =="ch💬Chats⬅":
            em3 = disnake.Embed(title=f"ch💬Chats⬅", description="```py\nChatrooms. Ask questions, join the conversation, share ideas or research, or just mess around!`", color=disnake.Colour.dark_gold())
            em3.add_field(name="Main Chat💬", value="<#896207280117264434>")
            em3.add_field(name="💬", value="<#1035063759196135424>")
            em3.add_field(name="💬", value="<#943359218545721395>")
            em3.add_field(name="💬", value="<#1019752456999145553>")
            em3.add_field(name="💬", value="<#1022199154069471232>")
            em3.add_field(name="Navigation Code:",value="```py\nch```")
            await interaction.edit_original_message(embed=em3)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)
        
        elif self.values[0] =="flow💦Options Flow":
            em4 = disnake.Embed(title="",description=f"```py\nSet notifications here to recieve automatic order flow posts real-time and intraday.```", color=disnake.Colour.dark_gold())
            em4.add_field(name="💦",value="<#1035273203683172434>")
            em4.add_field(name="💦",value="<#1035273514250408037>")
            em4.add_field(name="Navigation Code:",value="```py\nflow```")
            await interaction.edit_original_message(embed=em4)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)
        
        elif self.values[0] =="tt🚀TradyTics Realtime Alerts":
            em5 = disnake.Embed(title="tt🚀TradyTics Realtime Alerts", description=f"```py\nPlay at your own risk. Very good return rates and play-calling. Definitely set notifications here to recieve the play alerts as soon as possible.```", color=disnake.Colour.dark_red())
            em5.add_field(name="🚀", value="<#1016372151596630016>")
            
            em5.add_field(name="tt🚀", value="<#1016369913759285338>")
            
            em5.add_field(name="tt🚀", value="<#1016369933187301416>")
            
            em5.add_field(name="tt🚀", value="<#1016369947829600297>")
            
            em5.add_field(name="tt🚀", value="<#1016369960810979388>")
            
                
            em5.add_field(name="tt🚀", value="<#1016369974945775666>")
            
                
            em5.add_field(name="tt🚀", value="<#1016369975864348673>")
            
            em5.add_field(name="tt🚀", value="<#1016369984768852090>")
            
            
            em5.add_field(name="tt🚀", value="<#1016369985867743394>")
            
                
            em5.add_field(name="tt🚀", value="<#1016372139802234991>")
            
                
            em5.add_field(name="tt🚀", value="<#1016372323051388999>")
            
                
            em5.add_field(name="tt🚀", value="<#1016372517251850360>")
            em5.add_field(name="Navigation Code:",value="```py\ntt```")
            await interaction.edit_original_message(embed=em5)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)

        
        elif self.values[0] =="fm📜Forums":
            em6 = disnake.Embed(title="fm📜Forums", description=f"```py\nForums are relatively new, and are a great place to spark conversation. Learn about technicals, markets, join a disucssion, or start your own discussions.```", color=disnake.Colour.dark_orange())
            em6.add_field(name="fm🧠",value="<#1019711610949996644> ```py\nForum Topics:``` <#1028520267305205811>    <#1019713167418458153>    <#1026817221663666236>    <#1020734566375362630>")
            em6.add_field(name="fm❓",value="<#1019642125442363483> ```py\nForum Topics:``` <#1019706068961591318>    <#1019707633134997556>    <#1019790741360349244>    <#1020527718837784687>\n\n<#1019735801413775481>    <#1024209030614360094>    <#1022005228951834634>    <#1028509757444730950>\n\n<#1019790351587889162>    <#1019643506920259594>")
            em6.add_field(name="fm🤖",value="<#1032051790432182294> ```py\nForum Topics:``` <#1032053051609059489>    <#1032053768231071776>")
            em6.add_field(name="fm📜",value="<#1020761776062738543> ```py\nForum Topics:``` <#1020762438372687973>    <#1020823240844791900>    <#1020822834920042557>    <#1020823436504870972>")
            em6.add_field(name="fm📜",value="<#1006354207294627952>")
            em6.add_field(name="fm📜",value="<#1022544320030572574> ```py\nForum topics:``` <#1022545349807702016>     <#1022546202190950532>     <#1022602221608775690>     <#1022547353779044402> \n\n<#1022548867822133380>     <#1022548401314877490>     <#1022549806738051092>\n\n<#375862240601047070>     <#1022550078818369667>     <#1022552203665363016>\n\n<#1022553103939141702>     <#1022599729802133514>     <#1022598010678546552>     <#1022598659264753776>")
            em6.add_field(name="fm📜", value="<#1028353042896130108>")
            em6.add_field(name="fm📜", value="<#1020521179796222023> | ```py\nForum Topics:``` <#375862240601047070>     <#1020528673851449344>    <#1020524901263736833>    <#1020533866504650853>\n\n<#1020526050544979998>    <#1020531730731507753>    <#1020527105563426886>")
            em6.add_field(name="fm📜", value="<#1020736388754313326> ```py\nForum Topics:``` <#1020743569411153930>    <#1020739768012783626>    <#1020746246354370692>    <#1020737393600499723>\n\n<#1020742475717017660>    <#1020741909146247219>    <#1020740766097752117>    <#1020738755998527648>\n\n <#1020744926981529690>")
            em6.add_field(name="NOTE:",value="```py\nIf the channels are showing 'deleted-channel' it's because you need to visit the parent forum first, and then open the posts and they will appear!```")
            em6.add_field(name="Navigation Code:",value="```py\nfm```")
            
            await interaction.edit_original_message(embed=em6)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)


        elif self.values[0] =="ut💡Utilities Sector":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="ut💡",value="<#1015399097500455013>")
            em.add_field(name="ut💡",value="<#1015399280221106217>")
            em.add_field(name="ut💡",value="<#1015399365394833499>")
            em.add_field(name="ut💡",value="<#1015399398794068151>")
            em.add_field(name="ut💡",value="<#1015399422269603880>")
            em.add_field(name="ut💡",value="<#1015405869929861130>")
            em.add_field(name="Navigation Code:",value="```py\nut```")
            await interaction.edit_original_message(f"</navigate channels:1034275861865705476>",embed=em)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)
        
        elif self.values[0] =="etf⚓ETF Sector":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="etf⚓",value="<#1015396437015674890>")
            em.add_field(name="Navigation Code:",value="```py\netf```")
            await interaction.edit_original_message(f"</navigate channels:1034275861865705476>",embed=em)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)
        
        elif self.values[0] =="cc🌒Consumer Cyclical Sector":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="cc🌒",value="<#1015399375171760289>")
            em.add_field(name="cc🌒",value="<#1015399522458931291>")
            em.add_field(name="cc🌒",value="<#1015399532336521226>")
            em.add_field(name="cc🌒",value="<#1015399748515156119>")
            em.add_field(name="cc🌒",value="<#1015399726960607292>")
            em.add_field(name="cc🌒",value="<#1015413980598124625>")
            em.add_field(name="cc🌒",value="<#1015414003884896256>")
            em.add_field(name="cc🌒",value="<#1015413991549452288>")
            em.add_field(name="cc🌒",value="<#1015414015956111480>")
            em.add_field(name="cc🌒",value="<#1015416056816345139>")
            em.add_field(name="cc🌒",value="<#1015416093826896013>")
            em.add_field(name="Navigation Code:",value="```py\ncc```")
            await interaction.edit_original_message(f"</navigate channels:1034275861865705476>",embed=em)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)


        elif self.values[0] =="fd📶Market & Social Feeds": 
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="fd📶",value="<#1015879298940416071>")
            em.add_field(name="fd📶",value="<#1014186460162822234>")
            em.add_field(name="fd📶",value="<#1009157079803637851>")
            em.add_field(name="fd📶",value="<#1013870207456006164>")
            em.add_field(name="fd📶",value="<#1014186417385115728>")
            em.add_field(name="fd📶",value="<#961095958295347200>")
            em.add_field(name="fd📶",value="<#1009157366769524747>")
            em.add_field(name="fd📶",value="<#1035211665991553074>")
            em.add_field(name="Navigation Code:",value="```py\nfd```")
            await interaction.edit_original_message(f"</navigate channels:1034275861865705476>",embed=em)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)

        
        elif self.values[0] =="rss🔊RSS Feeds":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="🔊",value="<#1019359742549823508>") 
            em.add_field(name="🔊",value="<#1019361403032834128>")
            em.add_field(name="🔊",value="<#1019360302250332301>")
            em.add_field(name="🔊",value="<#1019362367362060410>")
            em.add_field(name="🔊",value="<#1019366556997795910>")  
            em.add_field(name="🔊",value="<#1019360339856470146>")          
            em.add_field(name="🔊",value="<#1028667813168173167>")
            em.add_field(name="🔊",value="<#1028668345702166698>")
            em.add_field(name="Navigation Code:",value="```py\nrss```")
            await interaction.edit_original_message(embed=em)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)  


        elif self.values[0] =="nw🌐News Feeds":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="nw🌐", value="<#1015664603079921784>")
            em.add_field(name="nw🌐", value="<#1015660065119797328>")
            em.add_field(name="nw🌐", value="<#1015664808101695488>")
            em.add_field(name="nw🌐", value="<#1015666153915424908>")
            em.add_field(name="nw🌐", value="<#1015665900864667821>")
            em.add_field(name="nw🌐", value="<#1015662803304067193>")
            em.add_field(name="nw🌐", value="<#1015659953865883788>")
            em.add_field(name="nw🌐", value="<#1015662737856155658>")
            em.add_field(name="nw🌐", value="<#1015664213605241013>")
            em.add_field(name="nw🌐", value="<#1015662708353409044>")
            em.add_field(name="nw🌐", value="<#1015663288639565835>")
            em.add_field(name="nw🌐", value="<#1015660095440425000>")
            em.add_field(name="nw🌐", value="<#1015663984013226084>")
            em.add_field(name="nw🌐", value="<#1015660106261737523>")
            em.add_field(name="nw🌐", value="<#1015666701389529228>")
            em.add_field(name="nw🌐", value="<#1015660085353123910>")
            em.add_field(name="nw🌐", value="<#1015664634923061362>")
            em.add_field(name="nw🌐", value="<#1015667147143381072>")
            em.add_field(name="nw🌐", value="<#1015666000814940220>")
            em.add_field(name="nw🌐", value="<#1015665876118294528>")
            em.add_field(name="nw🌐", value="<#1015660043284258856>")
            em.add_field(name="nw🌐", value="<#1015665926634475650>")
            em.add_field(name="nw🌐", value="<#1015664577754701825>")
            em.add_field(name="nw🌐", value="<#1015663450296430672>")
            em.add_field(name="Navigation Code:",value="```py\nnw```")
            await interaction.edit_original_message(embed=em)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)  
        
        elif self.values[0] =="cs📣Communication Services Sector":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="cs📣",value="<#1015390439400034334>")
            em.add_field(name="cs📣",value="<#1015390848734724187>")
            em.add_field(name="cs📣",value="<#1015390936798351381>")
            em.add_field(name="cs📣",value="<#1015390977701183559>")
            em.add_field(name="cs📣",value="<#1015391118231339058>")
            em.add_field(name="cs📣",value="<#1015391238704332932>")
            em.add_field(name="Navigation Code:",value="```py\ncs```")
            await interaction.edit_original_message(embed=em)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)  

        elif self.values[0] =="re🏠Real Estate Sector":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="re🏠",value="<#1015398703357505646>")
            em.add_field(name="re🏠",value="<#1015398716062060544>")
            em.add_field(name="re🏠",value="<#1015398609556094986>")
            em.add_field(name="re🏠",value="<#1015398725801226260>")
            em.add_field(name="Navigation Code:",value="```py\nre```")
            await interaction.edit_original_message(embed=em)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)  
        
        elif self.values[0] =="he💉Healthcare Sector":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="he💉",value="<#1015398746453966879>")
            em.add_field(name="he💉",value="<#1015398872132091956>")
            em.add_field(name="he💉",value="<#1015398885214138438>")
            em.add_field(name="he💉",value="<#1015398912049299486>")
            em.add_field(name="he💉",value="<#1015398898971451512>")
            em.add_field(name="he💉",value="<#1015398924426674257>")
            em.add_field(name="Navigation Code:",value="```py\nhe```")
            await interaction.edit_original_message(embed=em)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)  
        elif self.values[0] =="te💿Technology Sector":
            emte = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            emte.add_field(name="te💿",value="<#1015398199785168927>")
            emte.add_field(name="te💿",value="<#1015398409051578418>")
            emte.add_field(name="te💿",value="<#1015398422087467008>")
            emte.add_field(name="te💿",value="<#1015398435656060978>")
            emte.add_field(name="te💿",value="<#1015398530900299806>")
            emte.add_field(name="te💿",value="<#1015398545249009715>")
            emte.add_field(name="te💿",value="<#1015398557668343928>")
            emte.add_field(name="te💿",value="<#1015398585120084018>")
            emte.add_field(name="te💿",value="<#1015398587737329714>")
            emte.add_field(name="te💿",value="<#1015400438541070398>")
            em.add_field(name="Navigation Code:",value="```py\nte```")
            await interaction.edit_original_message(embed=emte)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)  
        elif self.values[0] =="in🌆Industrials Sector": 
            emin = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            emin.add_field(name="in🌆",value="<#1015403820337070181>")
            emin.add_field(name="in🌆",value="<#1015403810249781298>")
            emin.add_field(name="in🌆",value="<#1015398188112420894>")
            emin.add_field(name="in🌆",value="<#1015398139026477156>")
            emin.add_field(name="in🌆",value="<#1015398169921720390>")
            emin.add_field(name="in🌆",value="<#1015398149768089640>")
            emin.add_field(name="in🌆",value="<#1015398129396371586>")
            emin.add_field(name="in🌆",value="<#1015398120248582205>")
            emin.add_field(name="in🌆",value="<#1015398159184314478>")
            emin.add_field(name="in🌆",value="<#1015398110626840606>")
            emin.add_field(name="in🌆",value="<#1015398089516912741>")
            emin.add_field(name="in🌆",value="<#1015398078464925736>")
            emin.add_field(name="in🌆",value="<#1015398068868362240>")
            emin.add_field(name="in🌆",value="<#1015398055266234448>")
            emin.add_field(name="in🌆",value="<#1015397859023147131>")
            emin.add_field(name="Navigation Code:",value="```py\nin```")
            await interaction.edit_original_message(embed=emin)    
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)   
        elif self.values[0] == "cd⛴️Consumer Defensive Sector":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="cd⛴️",value="<#1015394369483849758>")
            em.add_field(name="cd⛴️",value="<#1015394456943472740>")
            em.add_field(name="cd⛴️",value="<#1015394467068514304>")
            em.add_field(name="cd⛴️",value="<#1015394479336865792>")
            em.add_field(name="cd⛴️",value="<#1015394491319975998>")
            em.add_field(name="cd⛴️",value="<#1015394502808195203>")
            em.add_field(name="cd⛴️",value="<#1015394516229963807>")
            em.add_field(name="Navigation Code:",value="```py\ncd```")  
            await interaction.edit_original_message(embed=em)
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)  


        elif self.values[0] =="fs💰Financial Services Sector":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="fs💰",value="<#1015396231050182766>")
            em.add_field(name="fs💰",value="<#1015396387988447242>")
            em.add_field(name="fs💰",value="<#1015397024629268580>")
            em.add_field(name="fs💰",value="<#1015396402400084150>")
            em.add_field(name="fs💰",value="<#1015396459044143225>")
            em.add_field(name="fs💰",value="<#1015396425451962408>")
            em.add_field(name="fs💰",value="<#1015396414014107719>")
            em.add_field(name="fs💰",value="<#1015397020120391700>")
            em.add_field(name="fs💰",value="<#1015396854772531292>")
            em.add_field(name="fs💰",value="<#1015396867028291614>")
            em.add_field(name="Navigation Code:",value="```py\nfs```")
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)  
            await interaction.edit_original_message(embed=em)

        elif self.values[0] == "bm🧱Basic Materials Sector":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="bm🧱",value="<#1015391472121557022>")
            em.add_field(name="bm🧱",value="<#1015391504333807746>")
            em.add_field(name="bm🧱",value="<#1015392688511660142>")
            em.add_field(name="bm🧱",value="<#1015391494263291904>")
            em.add_field(name="bm🧱",value="<#1015391265870856252>")
            em.add_field(name="bm🧱",value="<#1015391482447921212>")
            em.add_field(name="bm🧱",value="<#1015391514458849342>")
            em.add_field(name="bm🧱",value="<#1015391524013477898>")
            em.add_field(name="Navigation Code:",value="```py\nbm```")
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)  
            await interaction.edit_original_message(embed=em)


        elif self.values[0] == "en⚡Energy Sector":
            em = disnake.Embed(title="Sector Monitoring", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
            em.add_field(name="en⚡",value="<#1015398944186056744>")
            em.add_field(name="en⚡",value="<#1015399058388561980>")
            em.add_field(name="en⚡",value="<#1015399068480045237>")
            em.add_field(name="Navigation Code:",value="```py\nen```")
            await interaction.send("</navigate channels:1034275861865705476>", ephemeral=True)  
            await interaction.edit_original_message(embed=em)

class PersistentView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(FUDSTOPMenu())


class MasterView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.clear_items()
        self.add_item(MasterDrop())


class MasterDrop(disnake.ui.Select):
    def __init__(self):
        options = [ 
            disnake.SelectOption(label="📊 Stock Commands", description="These commands are used to gather stock data."),
            disnake.SelectOption(label="💦 Flow Commands", description="Commands displaying options flow from Open BB."),
            disnake.SelectOption(label="📉 Charting Commands", description="Commands used to call stock charts to Discord."),
            disnake.SelectOption(label="💸 Earnings Commands", description="Commands used for earnings related data."),
            disnake.SelectOption(label="🫧 Streaming Commands", description="Commands that return real-time data."),
            disnake.SelectOption(label="🎱 Dark Pool Commands", description="Dark Pool Commands - Open BB Bot."),
            disnake.SelectOption(label="🔎 Analysis Commands", description="Analyze markets, situations, and trends."),
            disnake.SelectOption(label="🩸 Jasmy Commands", description="Jasmycoin related commands!"),
            disnake.SelectOption(label="🐂 Webull Commands", description="Commands using Webull's API!"),
            disnake.SelectOption(label="🪙 Economy Commands", description="Commands related to economic information / data."),
            disnake.SelectOption(label="🧠 Learning Commands", description="Commands used to learn several topics from discord to markets."),
            disnake.SelectOption(label="🕵️ Due Dilligence Commands", description="Due diligence commands from Open BB Bot."),

        ]

        super().__init__(
            placeholder="🇨 🇲 🇩  🤖  🇱 🇮 🇸 🇹",
            min_values=1,
            max_values=1,
            custom_id="cmdselector",
            options=options
        )
    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == "📊 Stock Commands":
            em = disnake.Embed(title="Stock Commands")
            em.add_field(name="🤖/stock shortinterest", value="```py\nDisplays current and historic short interest for a ticker.```\n</stock shortinterest:1036711345468477514>")
            em.add_field(name="🤖/stock ipos",value="```py\nDisplays the upcoming IPOs.```\n</stock ipos:1036711345468477514>"),
            em.add_field(name="🤖/stock capitalflow", value="```py\nShows capitalflow for a ticker broken down by player size.```\n</stock capitalflow:1036711345468477514>")
            em.add_field(name="🤖/stock orderflow",value="```py\nShows the current day's orderflow in terms of buy, sell, and neutral.```\n</stock orderflow:1036711345468477514>")
            em.add_field(name="🤖/stock liquidity", value="```py\nDisplays the liquidity level for a stock. 0 = lowest. 5 = highest.```\n</stock liquidity:1036711345468477514>")
            em.add_field(name="🤖/stock criminals", value="```py\nReturns the latest insider buys/sells from government officials.```\n</stock criminals:1036711345468477514>")
            em.add_field(name="🤖/stock leverage", value="```py\nReturns leverage stats fora  stock.```\n</stock leverage:1036711345468477514>")
            em.add_field(name="🤖/stock company_brief", value="```py\nReturns core information for a company - such as location & contact.```\n</stock company_brief:1036711345468477514>")
            em.add_field(name="🤖/stock insider_summary", value="```py\nReturns the latest insider summary information for a tciker.```\n</stock insider_summary:1036711345468477514>")
            em.add_field(name="🤖/stock institutions", value="```py\nReturns the top 10 institutional holders for a ticker.```\n</stock institutions:1036711345468477514>")
            view = disnake.ui.View()
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masterstock")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            
            await interaction.response.edit_message(view=view, embed=em)
        elif self.values[0] == "📉 Charting Commands":
            em = disnake.Embed(title="📉Charting Commands",description="```py\nThese commands are used to utilize charting right from discord.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
            em.add_field(name="Charting Timeframe Arguments:", value="```py\nAccepted timeframes:``` ```py\n 1-minute 2-minute, 3-minute, 4-minute, 5-minute, 6-minute, 10-minute, 15-minute, 20-minute, 30-minute, 45-minute, 1-hour, 2-hour, 3-hour, 4-hour, 6-hour, 8-hour, 12-hour, 1-day, 2-day, 3-day, 4-day, 5-day, 6-day, 1-week, 2-week, 3-week, 1-month, 2-month, 3-month, 4-month, 6-month, 1-year```",inline=False)
            em.add_field(name="Charting Indicators:", value="```py\nAccepted Indicators:``` ```py\n'AbandonedBaby' 'AccumulationSwingIndex', 'Accumulation/Distribution', 'Advance/DeclineRatio','Alligator', ArnaudLegouxMovingAverage, 'Aroon', Aroon Oscillator, ATR, ATRBands, ATRTrailingStop, 'AverageDirectionalMovementIndex', AveragePrice, AwesomeOscillator, BalanceofPower, BearishEngulfing, BearishHammer, BearishHaramiCross, BearishHarami, BearishInvertedHammer, 'BearishMarubozu', BearishSpinningTop, 'BollingerBands', BollingerBands%B, BollingerBandsWidth, BullishEngulfing, BullishHammer, BullishHaramiCross Pattern, Bullish Harami Pattern, Bullish Inverted Hammer Pattern, Bullish Marubozu Pattern, Bullish Spinning Top Pattern```",inline=False)
            em.add_field(name="Charting Indicators:", value="```py\nMore Accepted Indicators:``` ```py\n'Center of Gravity', Chaikin Money Flow Index, Chaikin Oscillator, ChaikinVolatility, ChandeForecast, ChandeKrollStop, Chande Momentum Oscillator, Chop Zone, Choppiness Index, CommodityChannelIndex, Connors RSI, Coppock, Coppock Curve, Correlation-Log, CorrelationCoefficient, CumulativeTick'")
            em.add_field(name="Charting Indicators:",value="```py\nMore Accepted Indicators:``` ```py\nDarkCloudCoverPattern DetrendedPriceOscillator, DirectionalMovement, DisparityOscillator, DojiPattern, DONCH, DonchainWidth, 'DoubleEMA', DownsideTasukiGap, DragonflyDoji, Ease of Movement, ElderRay, Elder'sForceIndex, ElliottWave, EMA, EMACross, Envelopes, EveningDojiStar, EveningStar, FisherTransform, ForceIndex, FullStochasticOscillator, GatorOscillator, GopalakrishnanRangeIndex, GravestoneDoji, GuppyMovingAverage, GuppyOscillator, 'Hangman', HighMinus Low, Highest High Volume, HistoricalVolatility, Hull MA, IchimokuCloud, Intraday MomentumIndex, KeltnerChannel, Klinger, KnowSureThing, LeastSquaresMovingAverage, LinearRegressionChannel, LinearRegressionCurve, LinearRegressionSlope, 'LowestLowVolume', 'MACross', MAwithEMACross, 'MACD', MajorityRule, MarketProfile, MassIndex, McGinleyDynamic, MedianPrice, MedianPrice, Momentum, MoneyFlowIndex, MoonPhases, 'MorningDojiStar', MorningStar, 'MovingAverage'```",inline=False)
            em.add_field(name="Charting Indicators:",value="```py\nMore Accepted Indicators:``` ```py\nMovingAverageAdaptive MovingAverageChannel, MovingAverageDouble, MovingAverageEnvelope, MovingAverage Hamming, MovingAverageMultiple, Negative Volume Index, 'OnBalanceVolume', 'ParabolicSAR', PerformanceIndex PiercingLinePattern, PivotPointsHighLow, PivotPointsStandard, PositiveVolumeIndex, PrettyGoodOscillator, PriceChannel, PriceMomentumOscillator, PriceOscillator, PriceROC, PriceVolumeTrend, PrimeNumberBands, PrimeNumberOscillator, PsychologicalLine, QstickIndicator, RandomWalk, Ratio, RaviOscillator, RelativeVolatility, 'RSI', Schaff, Shinohara, ShootingStar, SMIErgodicIndicator, SMIErgodicOscillator, SmoothedMovingAverage, Spread, StandardDeviation, StandardError, StandardErrorBands, Stochastic, 'StochasticRSI', Stoller AverageRangeChannelBands, 'Supertrend', 'SwingIndex'```",inline=False)
            em.add_field(name="Charting Indicators:", value="```py\nMore Accepted Indicators:``` ```py\nThreeBlackCrows 'Three White Soldiers Pattern', TimeSeriesMovingAverage, TradeVolumeIndex, 'TrendIntensity', TrendStrengthIndex, TriangularMovingAverage, TripleEMA, Triple ExponentialAverage, TripleMA, 'TrueStrengthIndicator', TweezerBottom, TweezerTop, TwiggsMoneyFlowIndex, TypicalPrice, UlcerIndex, UltimateOscillator, VariableMovingAverage, VIDYAMovingAverage, VigorIndex, VolatilityClose-to-Close, VolatilityIndex, VolatilityO-H-L-C, VolatilityZeroTrendClose-to-Close, VolumeOscillator, VolumeProfile, VolumeROC, VolumeUnderlay, Vortex, VSTOP, 'VWAP', 'VWMA', 'WeightedClose', 'Weighted Moving Average', Williams %R, WilliamsAlligator, WilliamsFractal, ZigZag```",inline=False)
            em.add_field(name="Chart Types and Styles:",value="```py\nAccepted Styles:``` ```py\nArea, Renko, Kagi, PF, Linebreak, Heikinashi, Hollow, Baseline, HiLo, Column, Logarithmic, Extended, Wide, Marketprofile``` ```py\nHeatmap arguments:\n Whale, Low, Normal, High```",inline=False)
            em.set_image(url="https://media.discordapp.net/attachments/896207280117264434/1039000855887761519/1667787507499-375862240601047070-2293.png?width=895&height=671")
            view=disnake.ui.View()
            view.add_item(MasterCommand().chartcommands)
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masterchart")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            await interaction.response.edit_message(view=view, embed=em)

        elif self.values[0] == "💸 Earnings Commands":
            view=disnake.ui.View()
            view.add_item(MasterCommand().earningscommands)
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masterearnings")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            em = disnake.Embed(title="💸 Earnings Commands",description="```py\nYou can use these commands for earnings-specific data.```", color=disnake.Colour.dark_blue(), url="https://www.fudstop.io")
            em.add_field(name="Earnings Projection", value="```py\nReturns a ticker's earnings projection as well as implied move.```\n</earnings projection:1036711345401372733>")
            em.add_field(name="Earnings Crush", value="```py\nReturns a ticker's projecting earnings crush. It will display a % of IV expected to be lost AFTER EARNINGS. A high number indicates earnings will likely be IV crushed.```\n</earnings crush:1036711345401372733>")
            em.add_field(name="Earnings Calendar", value="```py\nReturns a booklet that has upcoming earnings organized by premarket and after hours. Command Provided by Quant Data```\n</earnings calendar:911140318118838277>")
            em.add_field(name="Earnings Today", value="```py\nReturns the earnings scheduled for the current day.```\n</earnings today:911140318118838277>")
            em.add_field(name="Earnings Date", value="```py\nReturns a ticker's earnings projection as well as implied move.```\n</earnings date:911140318118838277>")
            em.add_field(name="Earnings Day of Week", value="```py\nReturns the tickers scheduled for a specific day of the week.```\n</earnings day-of-week:911140318118838277>")
            await interaction.response.edit_message(view=view, embed=em)
        elif self.values[0] == "🫧 Streaming Commands":
            view=disnake.ui.View()
            view.add_item(MasterCommand().streamingcommands)
            em = disnake.Embed(title="🫧 Streaming Commands",description="```py\nThese commands return live data for a period of time when called.```", color=disnake.Colour.fuchsia(), url="https://www.fudstop.io")
            em.add_field(name="Quote", value="```py\nStream TWO stock tickers live.```\n</stream quote:1036711345401372738>")
            em.add_field(name="Crypto", value="```py\nStream a crypto currency live.```\n</stream crypto:1036711345401372738>")
            em.add_field(name="Time and Sales", value="```py\nStream time and sales for a ticker in real time.```\n</stream time_and_sales:1036711345401372738>")
            em.add_field(name="Double Crypto", value="```py\nStream TWO crypto currencies live.```\n</stream double_crypto:1036711345401372738>")
            em.add_field(name="Double Crypto", value="```py\nStream TWO stock tickers live.```\n</stream double_quote:1036711345401372738>")
            em.add_field(name="Tits", value="```py\nYup - stream tits.```\n</stream tits:1036711345401372738>")
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masterstreaming")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            await interaction.response.edit_message(view=view, embed=em)
        elif self.values[0] == "🎱 Dark Pool Commands":
            view=disnake.ui.View()
            view.add_item(MasterCommand().darkpoolcommands)
            em = disnake.Embed(title="🎱 Dark Pool Commands",description="```py\nCommands for dark-pool data.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
            em.add_field(name="All DP", value="```py\nThis command calls the latest 15 dark pools.```\n</dp alldp:1004263746170011748>")
            em.add_field(name="Allprints", value="```py\nTop total block and dark pool data.```\n</dp topsum:1004263746170011748>")
            em.add_field(name="Topsum", value="```py\nLast 15 block trades.```\n</dp allblocks:1004263746170011748>")
            em.add_field(name="All Blocks", value="```py\nInput a date to look for the largest block trades for that date.```\n</dp bigprints:1004263746170011748>")
            em.add_field(name="Big Prints", value="```py\nLast 15 combo of dark pools and blocks.```\n</dp allprints:1004263746170011748>")
            em.add_field(name="Levels", value="```py\nBiggest levels for all prints over the last X days.```\n</dp levels:1004263746170011748>")
            em.add_field(name="Sectors", value="```py\nSummary of all prints by % market cap by sector.```\n</dp sectors:1004263746170011748>")
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masterdarkpool")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            await interaction.response.edit_message(view=view, embed=em)
        elif self.values[0] == "🔎 Analysis Commands":
            view=disnake.ui.View()
            view.add_item(MasterCommand().analysiscommands)
            em = disnake.Embed(title="🔎 Analysis Commands",description="```py\nCommands used for stock and options analysis as well as general market analysis.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
            em.add_field(name="Top_Shorts", value="```py\nReturns tickers with over 30% short interest.``` </analysis topshorts:1036711345401372740>")
            em.add_field(name="Gaps_Down", value="```py\nEnter a % and it returns tickers that have gapped down.``` </analysis gaps_down:1036711345401372740>")
            em.add_field(name="Gaps_up", value="```py\nEnter a % and it returns tickers that have gapped up.``` </analysis gaps_up:1036711345401372740>")
            em.add_field(name="Finscreen", value="```py\nUse the finscreener with several customizable options.``` </analysis finscreen:1036711345401372740>")
            em.add_field(name="Overbought_Gap", value="```py\nReturns tickers that have gapped up and are overbought in a downward channel.``` </analysis overbought_gap:1036711345401372740>")
            em.add_field(name="Rating", value="```py\nReturns the buy vs hold vs sell ratings for a ticker.``` </analysis rating:1036711345401372740>")
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masteranalysis")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            await interaction.response.edit_message(view=view, embed=em)

        elif self.values[0] == "🩸 Jasmy Commands":
            view=disnake.ui.View()
            view.add_item(MasterCommand().jasmycommands)
            em = disnake.Embed(title="🩸 Jasmy Commands",description="```py\nCommands for the beloved Jasmycoin.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
            em.add_field(name="Holders", value="```py\nReturns the current number of Jasmy Wallets.```\n</jasmy holders:1036711345401372735>")
            em.add_field(name="Price", value="```py\nStreams the current Jasmy price across 20 exchanges.```\n</jasmy price:1036711345401372735>")
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masterjasmy")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)

            await interaction.response.edit_message(view=view, embed=em)
        elif self.values[0] == "🐂 Webull Commands":
            view=disnake.ui.View()
            view.add_item(MasterCommand().webullcommands)
            em = disnake.Embed(title="🐂 Webull Commands",description="```py\nCommands specifically from Webull's API.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
            em.add_field(name="Cost", value="```py\nReturns the cost distribution profited shares proportion straight from Webull.```\n</webull cost:1036711345401372739>")
            em.add_field(name="Webull_Quote", value="```py\nPulls webull data to discord and gives pricing data and information.```\n</webull webull_quote:1036711345401372739>")
            em.add_field(name="Analysis Tools", value="```py\nLearn about Webull Analysis tools.```\n</webull analysis_tools:1036711345401372739>")
            em.add_field(name="Bid_ask_Spread", value="```py\nReturns educational material regarding the bid ask spread.```\n</webull bid_ask_spread:1036711345401372739>")
            em.add_field(name="News", value="```py\nSearch for news articles from within Webull's news database.```\n</webull news:1036711345401372739>")
            em.add_field(name="Graphics", value="```py\nSearch by keyword for a list of helpful graphics.```\n</webull graphics:1036711345401372739>")
            em.add_field(name="News", value="```py\nLearn how to read and customize your options chain in Webull.```\n</webull options_chain:1036711345401372739>")
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masterwebull")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            MasterCommand().webullcommands.callback = lambda interaction: interaction.response.send_message("</webull cost:1036711345401372739> | </webull webull_quote:1036711345401372739 | </webull analysis_tools:1036711345401372739>\n</webull bid_ask_spread:1036711345401372739> | </webull news:1036711345401372739> | </webull graphics:1036711345401372739>\n</webull options_chain:1036711345401372739>")
            await interaction.response.edit_message(view=view, embed=em)
        elif self.values[0] == "🪙 Economy Commands":
            view=disnake.ui.View()
            view.add_item(MasterCommand().economycommands)
            em = disnake.Embed(title="🪙 Economy Commands",description="```py\nImportant economic data such as inflation, jobless claims, repo, and more.```", color=disnake.Colour.yellow(), url="https://www.fudstop.io")
            em.add_field(name="Jobless_Claims", value="```py\nReturns latest and historic Jobless Numbers.```\n</economy jobless_claims:1036711345401372742>")
            em.add_field(name="Inflation", value="```py\nReturns inflation numbers with averaged and historic data.```\n</economy inflation:1036711345401372742>")
            em.add_field(name="AMBS", value="```py\nReturns amount of retail capital in money market funds.```\n</economy retail_repo:1036711345401372742>")
            em.add_field(name="Retail_Repo", value="```py\nReturns the latest roll, swap, new, or all agency mortgage backed securities.```\n</economy ambs:1036711345401372742>")
            em.add_field(name="Data", value="```py\nReturns a large list of economic data.```\n</economy data:1036711345401372742>")
            em.add_field(name="House_trades", value="```py\nReturns a list of the latest trades from the House.```\n</economy house_trades:1036711345401372742>")
            em.add_field(name="econ RevRepo", value="```py\nReturns the latest and historic Reverse Repo Data with differences.```\n</econ revrepo:1004263746111275130>")
            em.add_field(name="econ Calendar", value="```py\nDisplays a calendar of important economic events.```\n</econ calendar:1004263746111275130>")
            em.add_field(name="econ GlBonds", value="```py\nDisplays global bond data.```\n</econ glbonds:1004263746111275130>")
            em.add_field(name="econ USBonds", value="```py\nDisplays US bond data.```\n</econ usbonds:1004263746111275130>")
            em.add_field(name="econ YieldCurve", value="```py\nDisplays US Bond yield curve data.```\n</econ yieldcurve:1004263746111275130>")
            em.add_field(name="econ indices", value="```py\nDisplays US indices overview.```\n</econ indices:1004263746111275130>")
            em.add_field(name="econ currencies", value="```py\nDisplays global currency data.```\n</econ currencies:1004263746111275130>")
            em.add_field(name="econ fedrates", value="```py\nDisplays upcoming FOMC events and projected BPS hike percentage.```\n</econ fedrates:1004263746111275130>")
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="mastereconomy")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            await interaction.response.edit_message(view=view, embed=em)
        elif self.values[0] == "🧠 Learning Commands":
            view=disnake.ui.View()
            view.add_item(MasterCommand().learncommands)
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masterlearning")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            em = disnake.Embed(title="🧠 Learning Commands",description="```py\nImportant economic data such as inflation, jobless claims, repo, and more.```", color=disnake.Colour.yellow(), url="https://www.fudstop.io")
            em.add_field(name="Option_Strategies", value="```py\nLearn about different options strategies.```\n</learn option_strategies:1036711345468477510>")
            em.add_field(name="Calls", value="```py\nLearn about call options.```\n</learn calls:1036711345468477510>")
            em.add_field(name="Puts", value="```py\nLearn about put options.```\n</learn puts:1036711345468477510>")
            em.add_field(name="Candle_Patterns", value="```py\nLearn about different candlestick patterns.```\n</learn candle_patterns:1036711345401372742>")
            em.add_field(name="Core_Logic", value="```py\nLearn about the core logic and how it works.```\n</learn core_logic:1036711345401372742>")
            em.add_field(name="China", value="```py\nLearn about China's economic transformation.```\n</learn china:1036711345401372742>")
            em.add_field(name="Covered_Calls", value="```py\nLearn about selling calls to generate revenue.```\n</learn covered_calls:1036711345401372742>")
            em.add_field(name="ETFs", value="```py\nLearn about exchange traded funds.```\n</learn etfs:1036711345401372742>")
            em.add_field(name="Filings", value="```py\nLearn about different SEC filings.```\n</learn filings:1036711345401372742>")
            em.add_field(name="Options 101", value="```py\nTake the Options 101 course from the Options Industry Council.```\n</learn options_101:1036711345401372742>")
            em.add_field(name="Greeks", value="```py\nLearn about the greeks: delta, gamma, rho, vega, and theta.```\n</learn greeks:1036711345401372742>")
            em.add_field(name="Order_types", value="```py\nLearn about the different order types.```\n</learn order_types:1036711345401372742>")
            em.add_field(name="OCC", value="```py\nLearn about important filings out of the Options Clearing Corporation.```\n</learn occ:1036711345401372742>")
            em.add_field(name="FINRA", value="```py\nLearn about important FINRA filings.```\n</learn finra:1036711345401372742>")
            em.add_field(name="NSFR_ratio", value="```py\nLearn about the critical Net Stable Funding Ratio regarding big banks.```\n</learn nsfr_ratio:1036711345401372742>")
            em.add_field(name="Webull_School", value="```py\nLearn about the Webull App.```\n</learn webull_school:1036711345401372742>")
            await interaction.response.edit_message(view=view, embed=em)
        elif self.values[0] == "🕵️ Due Dilligence Commands":
            view=disnake.ui.View()
            view.add_item(MasterCommand().ddcommands)
            em = disnake.Embed(title="🕵️ Due Diligence Commands",description="```py\nThese commands are somewhat useful. I don't really ever use these much, but depending on your trading strategy or type of trading personality - these could be a good fit for you. I'd at least give them a shot.```", color=disnake.Colour.dark_magenta(), url="https://www.fudstop.io")
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masterdd")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            em.add_field(name="AH", value="```py\nDisplays After Hours Data for a ticker.```\n</dd ah:1004263746090324066>")
            em.add_field(name="Analyst", value="```py\nReturns analyst ratings for a ticker.```\n</dd analyst:1004263746090324066>")
            em.add_field(name="Bio", value="```py\nReturns the stock company's profile.```\n</dd bio:1004263746090324066>")
            em.add_field(name="Customer", value="```py\nDisplays customers of a company.```\n</dd customer:1004263746090324066>")
            em.add_field(name="ermove", value="```py\nDisplays implied move for a ticker based on option prices.```\n</dd ermove:1004263746090324066>")
            em.add_field(name="divinfo", value="```py\nDisplays dividend information for a ticker.```\n</dd divinfo:1004263746090324066>")
            em.add_field(name="earnings", value="```py\nPick a date and return the earnings scheduled for that day.```\n</dd earnings:1004263746090324066>")
            em.add_field(name="pm", value="```py\nDisplay premarket data for a stock.```\n</dd pm:1004263746090324066>")
            em.add_field(name="pt", value="```py\nDisplays a chart with price targets```\n</dd pt:1004263746090324066>")
            em.add_field(name="ytd", value="```py\nDisplays period performance for a stock.```\n</dd ytd:1004263746090324066>")
            em.add_field(name="sec", value="```py\nDisplays recent SEC filings.```\n</dd sec:1004263746090324066>")
            em.add_field(name="est", value="```py\nDisplays earnings estimates.```\n</dd est:1004263746090324066>")
            await interaction.response.edit_message(view=view, embed=em)
        elif self.values[0] == "💦 Flow Commands":
            view=disnake.ui.View()
            view.add_item(MasterCommand().flowcommands)
            em = disnake.Embed(title="💦 Flow Commands",description="```py\nThese commands are good for visualizing options flow intra.```", color=disnake.Colour.dark_magenta(), url="https://www.fudstop.io")
            switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="masterflow")
            switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
            view.add_item(switcher)
            em = disnake.Embed(title="💦 Flows",description="```py\nThese commands are for visualizing flow data for options.```", color=disnake.Colour.purple(), url="https://www.fudstop.io")
            em.add_field(name="Flow - Quant Data", value="```py\nThis command searches for options flow using Quant Data's database and returns the results.``` ```py\nAccepted Arguments:\n'ticker' 'size' 'premium' 'moneyness' 'contract-type' 'trade-consolidation-type' 'expiration' 'unusual' 'golden-sweep' 'opening-position'```\n</flow:910724015490998293>")
            em.add_field(name="Day", value="```py\nReturns the most recent flow for a stock.```\n</flow day:1004263746170011749>")
            em.add_field(name="Bigflow", value="```py\nReturns the top 20 flow tickers by premium.```\n</flow bigflow:1004263746170011749>")
            em.add_field(name="Sumexp", value="```py\nReturns flow summary by expiration date for a ticker.```\n</flow sumexp:1004263746170011749>")
            em.add_field(name="Opening", value="```py\nTop 20 flow tickers with opening condition met.```\n</flow opening:1004263746170011749>")
            em.add_field(name="Sumday", value="```py\nGraph the current day's premium for a stock.```\n</flow sumday:1004263746170011749>")
            em.add_field(name="Sumweek", value="```py\nGraph total premium weekly summary for a stock.```\n</flow sumweek:1004263746170011749>")
            em.add_field(name="Prem", value="```py\nReturns a chart with sum of premium per day by calls/puts.```\n</flow prem:1004263746170011749>")
            em.add_field(name="Unu", value="```py\nReturns unusual options trade with over 100k Premium.```\n</flow unu:1004263746170011749>")
            em.add_field(name="Weekly", value="```py\nTop 20 flow by premium for weekly expiring stocks.```\n</flow weekly:1004263746170011749>")
            em.add_field(name="Sectors", value="```py\nSummary by % market cap by Sector.```\n</flow sectors:1004263746170011749>")
            em.add_field(name="Sumtop", value="```py\nTop flow for the day for a stock calls vs puts.```\n</flow sumtop:1004263746170011749>")
            em.add_field(name="Summary", value="```py\nSummary of all flow by % market cap.```\n</flow summary:1004263746170011749>")
            await interaction.response.edit_message(view=view, embed=em)
class MasterCommand(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @disnake.ui.button(label="📊 Stock Commands", style=disnake.ButtonStyle.gray,custom_id="stockbutton")
    async def commands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="siwtcherstock")
        switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
        self.add_item(switcher)
        select = disnake.ui.Select(
            placeholder="🇸 🇹 🇴 🇨 🇰 📊 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="stockcmd",
            options=[ 
                disnake.SelectOption(label="🤖/stock shortinterest", description="Displays current and historic short interest for a ticker."),
                disnake.SelectOption(label="🤖/stock ipos",description="Displays the upcoming IPOs."),
                disnake.SelectOption(label="🤖/stock capitalflow", description="Shows capitalflow for a ticker broken down by player size."),
                disnake.SelectOption(label="🤖/stock orderflow",description="Shows the current day's orderflow in terms of buy, sell, and neutral."),
                disnake.SelectOption(label="🤖/stock liquidity", description="Displays the liquidity level for a stock. 0 = lowest. 5 = highest."),
                disnake.SelectOption(label="🤖/stock criminals", description="Returns the latest insider buys/sells from government officials."),
                disnake.SelectOption(label="🤖/stock leverage", description="Returns leverage stats fora  stock."),
                disnake.SelectOption(label="🤖/stock company_brief", description="Returns core information for a company - such as location & contact."),
                disnake.SelectOption(label="🤖/stock insider_summary", description="Returns the latest insider summary information for a tciker."),
                disnake.SelectOption(label="🤖/stock institutions", description="Returns the top 10 institutional holders for a ticker."),



            ]
        )
        em = disnake.Embed(title="📊 Commands",description="```py\nThese commands are used to retrieve data revolving around specific tickers. Use the dropdown below to select a command!```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
        try:
            self.add_item(select)
        except ValueError:
            self.remove_item(select)


            self.clear_items()


            self.add_item(select)
            self.add_item(MasterCommand().chartcommands)
        em.add_field(name="Capitalflow", value="```py\nReturns an overall picture of orderflow broken down by player size.```\n</stock capitalflow:1036711345468477514>")
        em.add_field(name="Shortinterest", value="```py\nDisplays current and historic short interest for a ticker.```\n</stock shortinerest:1036711345468477514>")
        em.add_field(name="Company_Brief", value="```py\nReturns core company information such as location and contact info.```\n</stock company_brief:1036711345468477514>")
        em.add_field(name="Liquidity", value="```py\nReturns the liqudity rating for a stock. Lowest = 0. Highest = 5.```\n</stock liquidity:1036711345468477514>")
        em.add_field(name="Leverage", value="```py\nDisplays the current leverage statistics for a ticker.```\n</stock leverage:1036711345468477514>")
        em.add_field(name="Insider_Summary", value="```py\nDisplays the latest insider buys from the House and Senate.```\n</stock criminals:1036711345468477514>")
        em.add_field(name="Orderflow", value="```py\nShows the current day's orderflow in terms of buy, sell, and neutral.```\n</stock criminals:1036711345468477514>")
        em.add_field(name="Institutions", value="```py\nDisplays the latest insider buys from the House and Senate.```\n</stock criminals:1036711345468477514>")


        await inter.response.edit_message(embed=em, view=self)

    @disnake.ui.button(label="💦 Flow Commands", style=disnake.ButtonStyle.gray,custom_id="flowbutton")
    async def flowcommands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="flowback")
        switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
        view.add_item(switcher)
        flowselect = disnake.ui.Select(
            placeholder="🇫 🇱 🇴 🇼 💦 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="flowsel",
            options = [
                disnake.SelectOption(label="💦 Flow", description="Searches Quant Data's flow database and returns the results."),
                disnake.SelectOption(label="💦 Day", description="Returns the most recent flow for a stock."),
                disnake.SelectOption(label="💦 Bigflow", description="Returns the top 20 flow tickers by premium."),
                disnake.SelectOption(label="💦 Opening", description="Top 20 flow tickers with opening condition met."),
                disnake.SelectOption(label="💦 Sumday", description="Returns flow summary by expiration date for a ticker."),
                disnake.SelectOption(label="💦 Sumweek", description="Graph total premium weekly summary for a stock."),
                disnake.SelectOption(label="💦 Sumexp", description="Searches Quant Data's flow database and returns the results."),
                disnake.SelectOption(label="💦 Prem", description="Returns a chart with sum of premium per day by calls/puts."),
                disnake.SelectOption(label="💦 Unu", description="Returns unusual options trade with over 100k Premium."),
                disnake.SelectOption(label="💦 Weekly", description="Top 20 flow by premium for weekly expiring stocks."),
                disnake.SelectOption(label="💦 Sectors", description="Summary by % market cap by Sector."),
                disnake.SelectOption(label="💦 Sumtop", description="Top flow for the day for a stock calls vs puts."),
                disnake.SelectOption(label="💦 Summary", description="Summary of all flow by % market cap."),])
        
        em = disnake.Embed(title="💦 Flows",description="```py\nThese commands are for visualizing flow data for options.```", color=disnake.Colour.dark_teal(), url="https://www.fudstop.io")
        em.add_field(name="Flow - Quant Data", value="```py\nThis command searches for options flow using Quant Data's database and returns the results.``` ```py\nAccepted Arguments:\n'ticker' 'size' 'premium' 'moneyness' 'contract-type' 'trade-consolidation-type' 'expiration' 'unusual' 'golden-sweep' 'opening-position'```\n</flow:910724015490998293>")
        em.add_field(name="Day", value="```py\nReturns the most recent flow for a stock.```\n</flow day:1004263746170011749>")
        em.add_field(name="Bigflow", value="```py\nReturns the top 20 flow tickers by premium.```\n</flow bigflow:1004263746170011749>")
        em.add_field(name="Sumexp", value="```py\nReturns flow summary by expiration date for a ticker.```\n</flow sumexp:1004263746170011749>")
        em.add_field(name="Opening", value="```py\nTop 20 flow tickers with opening condition met.```\n</flow opening:1004263746170011749>")
        em.add_field(name="Sumday", value="```py\nGraph the current day's premium for a stock.```\n</flow sumday:1004263746170011749>")
        em.add_field(name="Sumweek", value="```py\nGraph total premium weekly summary for a stock.```\n</flow sumweek:1004263746170011749>")
        em.add_field(name="Prem", value="```py\nReturns a chart with sum of premium per day by calls/puts.```\n</flow prem:1004263746170011749>")
        em.add_field(name="Unu", value="```py\nReturns unusual options trade with over 100k Premium.```\n</flow unu:1004263746170011749>")
        em.add_field(name="Weekly", value="```py\nTop 20 flow by premium for weekly expiring stocks.```\n</flow weekly:1004263746170011749>")
        em.add_field(name="Sectors", value="```py\nSummary by % market cap by Sector.```\n</flow sectors:1004263746170011749>")
        em.add_field(name="Sumtop", value="```py\nTop flow for the day for a stock calls vs puts.```\n</flow sumtop:1004263746170011749>")
        em.add_field(name="Summary", value="```py\nSummary of all flow by % market cap.```\n</flow summary:1004263746170011749>")
        
        try:
            view.add_item(flowselect)
        except ValueError:
            view.remove_item(flowselect)


            view.clear_items()


            view.add_item(flowselect)

        flowselect.callback = lambda interaction: interaction.response.send_message("```py\nClick a command to use it!```</flow summary:1004263746170011749>  |  </flow sumtop:1004263746170011749>  |  </flow sectors:1004263746170011749>\n"
        "</flow weekly:1004263746170011749>  |  </flow unu:1004263746170011749>  |  </flow prem:1004263746170011749>\n</flow sumweek:1004263746170011749>  | </flow sumday:1004263746170011749>  | </flow opening:1004263746170011749>\n"
        "</flow sumexp:1004263746170011749> | </flow bigflow:1004263746170011749> | </flow day:1004263746170011749>\n </flow:910724015490998293>", ephemeral=True)
        await inter.response.edit_message(embed=em, view=view)
    @disnake.ui.button(label="📉 Charting Commands", style=disnake.ButtonStyle.gray,custom_id="chartbutton")
    async def chartcommands(self, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red,custom_id="switcherchart")
        switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
        self.add_item(switcher)
        select21 = disnake.ui.Select(
            placeholder="🇨 🇭 🇦 🇷 🇹 📉 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="chartingsel",
            options=[ 
                disnake.SelectOption(label="/c", description="Use the gigantic list below for a list of arguments."),

    
            ]
        )
        em = disnake.Embed(title="📉Charting Commands",description="```py\nThese commands are used to utilize charting right from discord.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
        em.add_field(name="Charting Timeframe Arguments:", value="```py\nAccepted timeframes:``` ```py\n 1-minute 2-minute, 3-minute, 4-minute, 5-minute, 6-minute, 10-minute, 15-minute, 20-minute, 30-minute, 45-minute, 1-hour, 2-hour, 3-hour, 4-hour, 6-hour, 8-hour, 12-hour, 1-day, 2-day, 3-day, 4-day, 5-day, 6-day, 1-week, 2-week, 3-week, 1-month, 2-month, 3-month, 4-month, 6-month, 1-year```",inline=False)
        em.add_field(name="Charting Indicators:", value="```py\nAccepted Indicators:``` ```py\n'AbandonedBaby' 'AccumulationSwingIndex', 'Accumulation/Distribution', 'Advance/DeclineRatio','Alligator', ArnaudLegouxMovingAverage, 'Aroon', Aroon Oscillator, ATR, ATRBands, ATRTrailingStop, 'Average DirectionalMovementIndex', AveragePrice, AwesomeOscillator, BalanceofPower, BearishEngulfing, BearishHammer, BearishHaramiCross, BearishHarami, BearishInvertedHammer, 'BearishMarubozu', BearishSpinningTop, 'BollingerBands', BollingerBands%B, BollingerBandsWidth, BullishEngulfing, BullishHammer, BullishHaramiCross Pattern, Bullish Harami Pattern, Bullish Inverted Hammer Pattern, Bullish Marubozu Pattern, Bullish Spinning Top Pattern```",inline=False)
        em.add_field(name="Charting Indicators:", value="```py\nMore Accepted Indicators:``` ```py\n'Center of Gravity', Chaikin Money Flow Index, Chaikin Oscillator, ChaikinVolatility, ChandeForecast, ChandeKrollStop, Chande Momentum Oscillator, Chop Zone, Choppiness Index, CommodityChannelIndex, Connors RSI, Coppock, Coppock Curve, Correlation-Log, CorrelationCoefficient, CumulativeTick'")
        em.add_field(name="Charting Indicators:",value="```py\nMore Accepted Indicators:``` ```py\nDarkCloudCoverPattern DetrendedPriceOscillator, DirectionalMovement, DisparityOscillator, DojiPattern, DONCH, DonchainWidth, 'DoubleEMA', DownsideTasukiGap, DragonflyDoji, Ease of Movement, ElderRay, Elder'sForceIndex, Elliott Wave, EMA, EMACross, Envelopes, EveningDojiStar, Evening Star Pattern, Fisher Transform, Force Index, FullStochasticOscillator, GatorOscillator, GopalakrishnanRangeIndex, GravestoneDoji, GuppyMovingAverage, GuppyOscillator, 'Hangman', HighMinus Low, Highest High Volume, HistoricalVolatility, Hull MA, IchimokuCloud, Intraday MomentumIndex, KeltnerChannel, Klinger, KnowSureThing, LeastSquaresMovingAverage, LinearRegressionChannel, LinearRegressionCurve, LinearRegressionSlope, 'LowestLowVolume', 'MACross', MAwithEMACross, 'MACD', MajorityRule, MarketProfile, MassIndex, McGinleyDynamic, MedianPrice, MedianPrice, Momentum, MoneyFlowIndex, MoonPhases, 'MorningDojiStar', MorningStar, 'MovingAverage'```",inline=False)
        em.add_field(name="Charting Indicators:",value="```py\nMore Accepted Indicators:``` ```py\nMovingAverageAdaptive MovingAverageChannel, MovingAverageDouble, MovingAverageEnvelope, MovingAverage Hamming, MovingAverageMultiple, Negative Volume Index, 'OnBalanceVolume', 'ParabolicSAR', PerformanceIndex PiercingLinePattern, PivotPointsHighLow, PivotPointsStandard, PositiveVolumeIndex, PrettyGoodOscillator, PriceChannel, PriceMomentumOscillator, PriceOscillator, PriceROC, PriceVolumeTrend, PrimeNumberBands, PrimeNumberOscillator, PsychologicalLine, QstickIndicator, RandomWalk, Ratio, RaviOscillator, RelativeVolatility, 'RSI', Schaff, Shinohara, ShootingStar, SMIErgodicIndicator, SMI Ergodic Oscillator, SmoothedMovingAverage, Spread, StandardDeviation, StandardError, StandardErrorBands, Stochastic, 'StochasticRSI', Stoller AverageRangeChannelBands, 'Supertrend', 'SwingIndex'```",inline=False)
        em.add_field(name="Charting Indicators:", value="```py\nMore Accepted Indicators:``` ```py\nThreeBlackCrows 'Three White Soldiers Pattern', TimeSeriesMovingAverage, TradeVolumeIndex, 'TrendIntensity', TrendStrengthIndex, TriangularMovingAverage, TripleEMA, Triple ExponentialAverage, TripleMA, 'TrueStrengthIndicator', TweezerBottom, TweezerTop, TwiggsMoneyFlowIndex, TypicalPrice, UlcerIndex, UltimateOscillator, VariableMovingAverage, VIDYAMovingAverage, VigorIndex, VolatilityClose-to-Close, VolatilityIndex, VolatilityO-H-L-C, VolatilityZeroTrendClose-to-Close, VolumeOscillator, VolumeProfile, VolumeROC, VolumeUnderlay, Vortex, VSTOP, 'VWAP', 'VWMA', 'WeightedClose', 'Weighted Moving Average', Williams %R, WilliamsAlligator, WilliamsFractal, ZigZag```",inline=False)
        em.add_field(name="Chart Types and Styles:",value="```py\nAccepted Styles:``` ```py\nArea, Renko, Kagi, PF, Linebreak, Heikinashi, Hollow, Baseline, HiLo, Column, Logarithmic, Extended, Wide, Marketprofile``` ```py\nHeatmap arguments:\n Whale, Low, Normal, High```",inline=False)
        em.set_image(url="https://media.discordapp.net/attachments/896207280117264434/1039000855887761519/1667787507499-375862240601047070-2293.png?width=895&height=671")
        try:
            self.add_item(select21)
        except ValueError:
            self.remove_item(select21)
            self.clear_items()

            self.add_item(select21)

        await inter.response.edit_message(embed=em, view=view)

    @disnake.ui.button(label="💸 Earnings Commands", style=disnake.ButtonStyle.gray,custom_id="earningsbutton")
    async def earningscommands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        switcher = disnake.ui.Button(label="🔙🅱️ 🇦 🇨 🇰", style=disnake.ButtonStyle.red, custom_id="switcherearnings")
        switcher.callback = lambda interaction: interaction.response.edit_message(view=MasterView())
        self.add_item(switcher)
        select4 = disnake.ui.Select(
            placeholder="🇪 🇦 🇷 🇳 🇮 🇳 🇬 🇸 💸 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="earningscmd",
            options=[ 
                disnake.SelectOption(label="Earnings Projection", description="Returns a ticker's earnings projection as well as implied move."),
                disnake.SelectOption(label="Earnings Crush", description="Returns a ticker's projecting earnings crush."),
                disnake.SelectOption(label="Earnings Calendar", description="Returns a ticker's projecting earnings crush."),
                disnake.SelectOption(label="Earnings Today", description="Returns all tickers with earnings for the current day."),
                disnake.SelectOption(label="Earnings Date", description="Select a date and return the earnings scheduled for that date."),

            ]
        )
        em = disnake.Embed(title="💸 Earnings Commands",description="```py\nYou can use these commands for earnings-specific data.```", color=disnake.Colour.dark_blue(), url="https://www.fudstop.io")
        em.add_field(name="Earnings Projection", value="```py\nReturns a ticker's earnings projection as well as implied move.```\n</earnings projection:1036711345401372733>")
        em.add_field(name="Earnings Crush", value="```py\nReturns a ticker's projecting earnings crush. It will display a % of IV expected to be lost AFTER EARNINGS. A high number indicates earnings will likely be IV crushed.```\n</earnings crush:1036711345401372733>")
        em.add_field(name="Earnings Calendar", value="```py\nReturns a booklet that has upcoming earnings organized by premarket and after hours. Command Provided by Quant Data```\n</earnings calendar:911140318118838277>")
        em.add_field(name="Earnings Today", value="```py\nReturns the earnings scheduled for the current day.```\n</earnings today:911140318118838277>")
        em.add_field(name="Earnings Date", value="```py\nReturns a ticker's earnings projection as well as implied move.```\n</earnings date:911140318118838277>")
        em.add_field(name="Earnings Day of Week", value="```py\nReturns the tickers scheduled for a specific day of the week.```\n</earnings day-of-week:911140318118838277>")

        try:
            self.add_item(select4)
        
        except ValueError:
            self.remove_item(select4)
            self.clear_items()
        
            self.add_item(select4)

            
            

        await inter.response.edit_message(embed=em, view=self)


    @disnake.ui.button(label="🫧 Streaming Commands", style=disnake.ButtonStyle.gray,row=1,custom_id="streambutton")
    async def streamingcommands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        select3 = disnake.ui.Select(
            placeholder="🇸 🇹 🇷 🇪 🇦 🇲 🫧 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="streamcmds",
            options=[ 
                disnake.SelectOption(label="🫧Time and Sales", description="Stream time and sales in real time."),
                disnake.SelectOption(label="🫧Quote", description="Stream a stock quote live."),
                disnake.SelectOption(label="🫧Crypto", description="Stream crypto live."),
                disnake.SelectOption(label="🫧Double Crypto", description="Stream two cryptos live - simultaneously."),
                disnake.SelectOption(label="🫧Double Quote", description="Stream two stocks live - simultaneously."),
                disnake.SelectOption(label="🫧Tits", description="Stream some tits."),

            ]
        )
        em = disnake.Embed(title="🫧 Streaming Commands",description="```py\nThese commands return live data for a period of time when called.```", color=disnake.Colour.fuchsia(), url="https://www.fudstop.io")
        em.add_field(name="Quote", value="```py\nStream TWO stock tickers live.```\n</stream quote:1036711345401372738>")
        em.add_field(name="Crypto", value="```py\nStream a crypto currency live.```\n</stream crypto:1036711345401372738>")
        em.add_field(name="Time and Sales", value="```py\nStream time and sales for a ticker in real time.```\n</stream time_and_sales:1036711345401372738>")
        em.add_field(name="Double Crypto", value="```py\nStream TWO crypto currencies live.```\n</stream double_crypto:1036711345401372738>")
        em.add_field(name="Double Crypto", value="```py\nStream TWO stock tickers live.```\n</stream double_quote:1036711345401372738>")
        em.add_field(name="Tits", value="```py\nYup - stream tits.```\n</stream tits:1036711345401372738>")
        try:
            self.add_item(select3)
        except ValueError:
            self.remove_item(select3)
            self.clear_items()


            self.add_item(select3)
            self.add_item(MasterCommand().earningscommands)
            self.add_item(MasterCommand().chartcommands)
            self.add_item(MasterCommand().darkpoolcommands)
        
        
        
        await inter.response.edit_message(embed=em, view=self)

    @disnake.ui.button(label="🎱 Dark Pool Commands", style=disnake.ButtonStyle.gray,row=1,custom_id="dpoolbutton")
    async def darkpoolcommands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        select2 = disnake.ui.Select(
            placeholder="🇩 🇦 🇷 🇰 🇵 🇴 🇴 🇱 🎱 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="dpoolcmds",
            options=[ 
                disnake.SelectOption(label="🎱All DP", description="Returns the last 15 dark pools."),
                disnake.SelectOption(label="🎱Allprints", description="Last 15 combo of dark pools and blocks."),
                disnake.SelectOption(label="🎱Topsum", description="Top total block and dark pool data."),
                disnake.SelectOption(label="🎱All Blocks", description="Last 15 block trades."),
                disnake.SelectOption(label="🎱Big Prints", description="Input a date to look for the largest block trades for that date."),
                disnake.SelectOption(label="🎱Levels", description="Biggest levels for all prints over the last X days."),
                disnake.SelectOption(label="🎱Sectors", description="Summary of all prints by % market cap by sector."),

            ]
        )
        em = disnake.Embed(title="🎱 Dark Pool Commands",description="```py\nCommands for dark-pool data.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
        em.add_field(name="All DP", value="```py\nThis command calls the latest 15 dark pools.```\n</dp alldp:1004263746170011748>")
        em.add_field(name="Allprints", value="```py\nTop total block and dark pool data.```\n</dp topsum:1004263746170011748>")
        em.add_field(name="Topsum", value="```py\nLast 15 block trades.```\n</dp allblocks:1004263746170011748>")
        em.add_field(name="All Blocks", value="```py\nInput a date to look for the largest block trades for that date.```\n</dp bigprints:1004263746170011748>")
        em.add_field(name="Big Prints", value="```py\nLast 15 combo of dark pools and blocks.```\n</dp allprints:1004263746170011748>")
        em.add_field(name="Levels", value="```py\nBiggest levels for all prints over the last X days.```\n</dp levels:1004263746170011748>")
        em.add_field(name="Sectors", value="```py\nSummary of all prints by % market cap by sector.```\n</dp sectors:1004263746170011748>")
        try:
            self.add_item(select2)
        except ValueError:
            self.remove_item(select2)
            self.clear_items()


            self.add_item(select2)
            self.add_item(MasterCommand().earningscommands)
            self.add_item(MasterCommand().chartcommands)
            self.add_item(MasterCommand().commands)
        await inter.response.edit_message(embed=em, view=self)



    @disnake.ui.button(label="🔎 Analysis Commands", style=disnake.ButtonStyle.gray, row=2,custom_id="analysisbutton")
    async def analysiscommands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        select5 = disnake.ui.Select(
            placeholder="🇦 🇳 🇦 🇱 🇾 🇸 🇮 🇸 🔎 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="analysiscmd",
            options=[ 
                disnake.SelectOption(label="🔎TopShorts", description="Returns tickers with over 30% short interest."),
                disnake.SelectOption(label="🔎Gaps_Down", description="Enter a % and it returns tickers that have gapped down."),
                disnake.SelectOption(label="🔎Gaps_Up", description="Enter a % and it returns tickers that have gapped up."),
                disnake.SelectOption(label="🔎Finscreen", description="Use the finscreener with several customizable options."),
                disnake.SelectOption(label="🔎Overbought_Gap", description="Returns tickers that have gapped up and are overbought in a downward channel."),
                disnake.SelectOption(label="🔎Rating", description="Returns the buy vs hold vs sell ratings for a ticker."),
  
            ]
        )
        em = disnake.Embed(title="🔎 Analysis Commands",description="```py\nCommands used for stock and options analysis as well as general market analysis.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
        em.add_field(name="Top Shorts", value="```py\nReturns tickers with over 30% short interest.``` </analysis topshorts:1036711345401372740>")
        em.add_field(name="Top Shorts", value="```py\nEnter a % and it returns tickers that have gapped down.``` </analysis gaps_down:1036711345401372740>")
        em.add_field(name="Top Shorts", value="```py\nEnter a % and it returns tickers that have gapped up.``` </analysis gaps_up:1036711345401372740>")
        em.add_field(name="Top Shorts", value="```py\nUse the finscreener with several customizable options.``` </analysis finscreen:1036711345401372740>")
        em.add_field(name="Top Shorts", value="```py\nReturns tickers that have gapped up and are overbought in a downward channel.``` </analysis overbought_gap:1036711345401372740>")
        em.add_field(name="Top Shorts", value="```py\nReturns the buy vs hold vs sell ratings for a ticker.``` </analysis rating:1036711345401372740>")
        try:
            self.add_item(select5)
        except ValueError:
            self.clear_items()
            self.add_item(select5)
            self.add_item(MasterCommand().darkpoolcommands)
            self.add_item(MasterCommand().earningscommands)
            self.add_item(MasterCommand().commands)

        await inter.response.edit_message(embed=em, view=self)




    @disnake.ui.button(label="🔎 Analysis Commands", style=disnake.ButtonStyle.gray, row=2,custom_id="analysisbutton")
    async def analysiscommands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        select5 = disnake.ui.Select(
            placeholder="🇦 🇳 🇦 🇱 🇾 🇸 🇮 🇸 🔎 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="analysiscmd",
            options=[ 
                disnake.SelectOption(label="🔎TopShorts", description="Returns tickers with over 30% short interest."),
                disnake.SelectOption(label="🔎Gaps_Down", description="Enter a % and it returns tickers that have gapped down."),
                disnake.SelectOption(label="🔎Gaps_Up", description="Enter a % and it returns tickers that have gapped up."),
                disnake.SelectOption(label="🔎Finscreen", description="Use the finscreener with several customizable options."),
                disnake.SelectOption(label="🔎Overbought_Gap", description="Returns tickers that have gapped up and are overbought in a downward channel."),
                disnake.SelectOption(label="🔎Rating", description="Returns the buy vs hold vs sell ratings for a ticker."),
  
            ]
        )
        em = disnake.Embed(title="🔎 Analysis Commands",description="```py\nCommands used for stock and options analysis as well as general market analysis.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
        em.add_field(name="Top Shorts", value="```py\nReturns tickers with over 30% short interest.``` </analysis topshorts:1036711345401372740>")
        em.add_field(name="Top Shorts", value="```py\nEnter a % and it returns tickers that have gapped down.``` </analysis gaps_down:1036711345401372740>")
        em.add_field(name="Top Shorts", value="```py\nEnter a % and it returns tickers that have gapped up.``` </analysis gaps_up:1036711345401372740>")
        em.add_field(name="Top Shorts", value="```py\nUse the finscreener with several customizable options.``` </analysis finscreen:1036711345401372740>")
        em.add_field(name="Top Shorts", value="```py\nReturns tickers that have gapped up and are overbought in a downward channel.``` </analysis overbought_gap:1036711345401372740>")
        em.add_field(name="Top Shorts", value="```py\nReturns the buy vs hold vs sell ratings for a ticker.``` </analysis rating:1036711345401372740>")
        try:
            self.add_item(select5)
        except ValueError:
            self.clear_items()
            self.add_item(select5)
            self.add_item(MasterCommand().darkpoolcommands)
            self.add_item(MasterCommand().earningscommands)
            self.add_item(MasterCommand().commands)

        await inter.response.edit_message(embed=em, view=self)



    @disnake.ui.button(label="🩸 Jasmy Commands", style=disnake.ButtonStyle.gray,row=2,custom_id="jasmybutton")
    async def jasmycommands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        select55 = disnake.ui.Select(
            placeholder="🇯 🇦 🇸 🇲 🇾 🩸 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="jasmycmd",
            options=[ 
                disnake.SelectOption(label="🩸Holders", description="Returns the current number of Jasmy Wallets."),
                disnake.SelectOption(label="🩸Price", description="Streams the current Jasmy price across 20 exchanges."),
                disnake.SelectOption(label="🩸", description=""),

            ]
        )
        em = disnake.Embed(title="🩸 Jasmy Commands",description="```py\nCommands for the beloved Jasmycoin.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
        em.add_field(name="Holders", value="```py\nReturns the current number of Jasmy Wallets.```\n</jasmy holders:1036711345401372735>")
        em.add_field(name="Price", value="```py\nStreams the current Jasmy price across 20 exchanges.```\n</jasmy price:1036711345401372735>")
        try:
            self.add_item(select55)
        except ValueError:
            self.remove_item(select55)
            self.clear_items()

            self.add_item(select55)
            self.add_item(MasterCommand().earningscommands)
            self.add_item(MasterCommand().streamingcommands)
            self.add_item(MasterCommand().darkpoolcommands)

        await inter.response.edit_message(embed=em, view=self)


    @disnake.ui.button(label="🐂 Webull Commands", style=disnake.ButtonStyle.gray,row=2,custom_id="webullbutton")
    async def webullcommands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        select9 = disnake.ui.Select(
            placeholder="🇼 🇪 🇧 🇺 🇱 🇱 🐂 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="webullcmds",
            options=[ 
                disnake.SelectOption(label="🐂Cost", description="Returns the cost distribution profited shares proportion straight from Webull."),
                disnake.SelectOption(label="🐂Webull_Quote", description="Pulls webull data to discord and gives pricing data and information."),
                disnake.SelectOption(label="🐂Analysis_Tools", description="Learn about Webull's analysis tools."),
                disnake.SelectOption(label="🐂Bid_Ask_Spread", description="Returns educational material regarding the bid ask spread."),
                disnake.SelectOption(label="🐂News", description="Search for news articles from within Webull's news database."),
                disnake.SelectOption(label="🐂Graphics", description="Search by keyword for a list of helpful graphics."),
                disnake.SelectOption(label="🐂Options_Chain", description="Learn how to read and customize your options chain in Webull."),

            ]
        )
        em = disnake.Embed(title="🐂 Webull Commands",description="```py\nCommands specifically from Webull's API.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
        em.add_field(name="Cost", value="```py\nReturns the cost distribution profited shares proportion straight from Webull.```\n</webull cost:1036711345401372739>")
        em.add_field(name="Webull_Quote", value="```py\nPulls webull data to discord and gives pricing data and information.```\n</webull webull_quote:1036711345401372739>")
        em.add_field(name="Analysis Tools", value="```py\nLearn about Webull Analysis tools.```\n</webull analysis_tools:1036711345401372739>")
        em.add_field(name="Bid_ask_Spread", value="```py\nReturns educational material regarding the bid ask spread.```\n</webull bid_ask_spread:1036711345401372739>")
        em.add_field(name="News", value="```py\nSearch for news articles from within Webull's news database.```\n</webull news:1036711345401372739>")
        em.add_field(name="Graphics", value="```py\nSearch by keyword for a list of helpful graphics.```\n</webull graphics:1036711345401372739>")
        em.add_field(name="News", value="```py\nLearn how to read and customize your options chain in Webull.```\n</webull options_chain:1036711345401372739>")
        try:
            self.add_item(select9)
        except ValueError:
            self.clear_items()
            self.add_item(select9)

        
        select9.callback = lambda interaction: interaction.response.edit_message(view=MasterCommand())

        await inter.response.edit_message(embed=em, view=self)


    @disnake.ui.button(label="🪙 Economy Commands", style=disnake.ButtonStyle.gray,row=2, custom_id="econbutton")
    async def economycommands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        select10 = disnake.ui.Select(
            placeholder="🇴 🇵 🇹 🇮 🇴 🇳 🇸 🪙 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="econcmds",
            options=[ 
                disnake.SelectOption(label="🪙Jobless Claims", description="Returns latest and historic Jobless Numbers."),
                disnake.SelectOption(label="🪙Inflation", description="Returns latest and historic inflation numbers with averages"),
                disnake.SelectOption(label="🪙AMBS", description="Returns the latest roll, swap, new, or all agency mortgage backed securities."),
                disnake.SelectOption(label="🪙Retail_Repo", description="Returns the amount of retail capital in money market funds."),
                disnake.SelectOption(label="🪙Data", description="Returns a large list of economic data."),
                disnake.SelectOption(label="🪙House_Trades", description="Returns a list of the latest trades from the House."),
                disnake.SelectOption(label="🪙econ revrepo", description="Returns the latest and historic Reverse Repo Data with differences."),
                disnake.SelectOption(label="🪙econ calendar", description="Displays a calendar of important economic events."),
                disnake.SelectOption(label="🪙econ glbonds", description="Displays global bond data."),
                disnake.SelectOption(label="🪙econ usbonds", description="Displays US bond data."),
                disnake.SelectOption(label="🪙econ yieldcurve", description="Displays US Bond yield curve data."),
                disnake.SelectOption(label="🪙econ indices", description="Displays US indices overview."),
                disnake.SelectOption(label="🪙econ currencies", description="Displays global currency data."),
                disnake.SelectOption(label="🪙econ fedrates", description="Displays upcoming FOMC events and projected BPS hike percentage."),
    
            ]
        )
        em = disnake.Embed(title="🪙 Economy Commands",description="```py\nImportant economic data such as inflation, jobless claims, repo, and more.```", color=disnake.Colour.yellow(), url="https://www.fudstop.io")
        em.add_field(name="Jobless_Claims", value="```py\nReturns latest and historic Jobless Numbers.```\n</economy jobless_claims:1036711345401372742>")
        em.add_field(name="Inflation", value="```py\nReturns inflation numbers with averaged and historic data.```\n</economy inflation:1036711345401372742>")
        em.add_field(name="AMBS", value="```py\nReturns amount of retail capital in money market funds.```\n</economy retail_repo:1036711345401372742>")
        em.add_field(name="Retail_Repo", value="```py\nReturns the latest roll, swap, new, or all agency mortgage backed securities.```\n</economy ambs:1036711345401372742>")
        em.add_field(name="Data", value="```py\nReturns a large list of economic data.```\n</economy data:1036711345401372742>")
        em.add_field(name="House_trades", value="```py\nReturns a list of the latest trades from the House.```\n</economy house_trades:1036711345401372742>")
        em.add_field(name="econ RevRepo", value="```py\nReturns the latest and historic Reverse Repo Data with differences.```\n</econ revrepo:1004263746111275130>")
        em.add_field(name="econ Calendar", value="```py\nDisplays a calendar of important economic events.```\n</econ calendar:1004263746111275130>")
        em.add_field(name="econ GlBonds", value="```py\nDisplays global bond data.```\n</econ glbonds:1004263746111275130>")
        em.add_field(name="econ USBonds", value="```py\nDisplays US bond data.```\n</econ usbonds:1004263746111275130>")
        em.add_field(name="econ YieldCurve", value="```py\nDisplays US Bond yield curve data.```\n</econ yieldcurve:1004263746111275130>")
        em.add_field(name="econ indices", value="```py\nDisplays US indices overview.```\n</econ indices:1004263746111275130>")
        em.add_field(name="econ currencies", value="```py\nDisplays global currency data.```\n</econ currencies:1004263746111275130>")
        em.add_field(name="econ fedrates", value="```py\nDisplays upcoming FOMC events and projected BPS hike percentage.```\n</econ fedrates:1004263746111275130>")

        try:
            self.add_item(select10)
        except ValueError:
            self.clear_items()
            self.add_item(select10)



        
        select10.callback = lambda interaction: interaction.response.edit_message(view=MasterCommand())



    @disnake.ui.button(label="🧠 Learning Commands", style=disnake.ButtonStyle.gray,row=1,custom_id="learnbutton")
    async def learncommands(self, inter: disnake.AppCmdInter):
        select11 = disnake.ui.Select(
            placeholder="🇱 🇪 🇦 🇷 🇳 🇮 🇳 🇬 🧠 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=5,
            max_values=5,
            custom_id="learncmds",
            options=[ 

                disnake.SelectOption(label="🧠Option_Strategies", description="Learn about different options strategies."),
                disnake.SelectOption(label="🧠Calls", description="Learn about call options."),
                disnake.SelectOption(label="🧠Puts", description="Learn about put options."),
                disnake.SelectOption(label="🧠Candle_patterns", description="Learn about different candlestick patterns."),
                disnake.SelectOption(label="🧠China", description=""),
                disnake.SelectOption(label="🧠Core Logic", description="Learn about the core logic and how it works."),
                disnake.SelectOption(label="🧠Covered_Calls", description="Learn about selling calls to generate revenue."),
                disnake.SelectOption(label="🧠SEC", description="Learn about different SEC filings."),
                disnake.SelectOption(label="🧠ETFs", description="Learn about Exchange Traded Funds."),
                disnake.SelectOption(label="🧠Greeks", description="Learn about the greeks: delta, gamma, rho, vega, and theta."),
                disnake.SelectOption(label="🧠Order_types", description="Learn about the different order types."),
                disnake.SelectOption(label="🧠Options_101", description="Take the Options 101 course from the Options Industry Council."),
                disnake.SelectOption(label="🧠OCC", description="Learn about important filings out of the Options Clearing Corporation."),
                disnake.SelectOption(label="🧠FINRA", description="Learn about important FINRA filings."),
                disnake.SelectOption(label="🧠NSFR_Ratio", description="Learn about the critical Net Stable Funding Ratio regarding big banks."),
                disnake.SelectOption(label="🧠webull_school", description="Learn about the Webull App."),

    
            ]
        )
        em = disnake.Embed(title="🧠 Learning Commands",description="```py\nImportant economic data such as inflation, jobless claims, repo, and more.```", color=disnake.Colour.yellow(), url="https://www.fudstop.io")
        em.add_field(name="Option_Strategies", value="```py\nLearn about different options strategies.```\n</learn option_strategies:1036711345468477510>")
        em.add_field(name="Calls", value="```py\nLearn about call options.```\n</learn calls:1036711345468477510>")
        em.add_field(name="Puts", value="```py\nLearn about put options.```\n</learn puts:1036711345468477510>")
        em.add_field(name="Candle_Patterns", value="```py\nLearn about different candlestick patterns.```\n</learn candle_patterns:1036711345401372742>")
        em.add_field(name="Core_Logic", value="```py\nLearn about the core logic and how it works.```\n</learn core_logic:1036711345401372742>")
        em.add_field(name="China", value="```py\nLearn about China's economic transformation.```\n</learn china:1036711345401372742>")
        em.add_field(name="Covered_Calls", value="```py\nLearn about selling calls to generate revenue.```\n</learn covered_calls:1036711345401372742>")
        em.add_field(name="ETFs", value="```py\nLearn about exchange traded funds.```\n</learn etfs:1036711345401372742>")
        em.add_field(name="Filings", value="```py\nLearn about different SEC filings.```\n</learn filings:1036711345401372742>")
        em.add_field(name="Options 101", value="```py\nTake the Options 101 course from the Options Industry Council.```\n</learn options_101:1036711345401372742>")
        em.add_field(name="Greeks", value="```py\nLearn about the greeks: delta, gamma, rho, vega, and theta.```\n</learn greeks:1036711345401372742>")
        em.add_field(name="Order_types", value="```py\nLearn about the different order types.```\n</learn order_types:1036711345401372742>")
        em.add_field(name="OCC", value="```py\nLearn about important filings out of the Options Clearing Corporation.```\n</learn occ:1036711345401372742>")
        em.add_field(name="FINRA", value="```py\nLearn about important FINRA filings.```\n</learn finra:1036711345401372742>")
        em.add_field(name="NSFR_ratio", value="```py\nLearn about the critical Net Stable Funding Ratio regarding big banks.```\n</learn nsfr_ratio:1036711345401372742>")
        em.add_field(name="Webull_School", value="```py\nLearn about the Webull App.```\n</learn webull_school:1036711345401372742>")




        try:
            self.add_item(select11)
        except ValueError:
            self.clear_items()
            self.add_item(select11)

        
        select11.callback = lambda interaction: interaction.response.edit_message(view=MasterCommand())


        await inter.response.edit_message(embed=em, view=self)





    @disnake.ui.button(label="🕵️ Due Dilligence", style=disnake.ButtonStyle.gray,row=1,custom_id="ddbutton")
    async def ddcommands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        select11 = disnake.ui.Select(
            placeholder="🇩 🇩 🕵️ 🇨 🇴 🇲 🇲 🇦 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="ddcmds",
            options=[ 

                disnake.SelectOption(label="🕵️AH", description="Displays After Hours Data for a ticker."),
                disnake.SelectOption(label="🕵️Analyst", description="Displays Analyst recommendations."),
                disnake.SelectOption(label="🕵️Bio", description="Displays a stock company's profile."),
                disnake.SelectOption(label="🕵️Customer", description="Displays customers of a company."),
                disnake.SelectOption(label="🕵️ermove", description="Displays implied move for a ticker based on option prices."),
                disnake.SelectOption(label="🕵️divinfo", description="Displays dividend information for a ticker."),
                disnake.SelectOption(label="🕵️earnings", description="Pick a date and return the earnings scheduled for that day."),
                disnake.SelectOption(label="🕵️PM", description="Display premarket data for a stock."),
                disnake.SelectOption(label="🕵️pt", description="Displays a chart with price targets"),
                disnake.SelectOption(label="🕵️ytd", description="Displays period performance for a stock."),
                disnake.SelectOption(label="🕵️sec", description="Dispalys latest SEC filings for a company."),
                disnake.SelectOption(label="🕵️est", description="Dispalys earnings estimates."),


    
            ]
        )
        em = disnake.Embed(title="🕵️ Due Diligence Commands",description="```py\nThese commands are somewhat useful. I don't really ever use these much, but depending on your trading strategy or type of trading personality - these could be a good fit for you. I'd at least give them a shot.```", color=disnake.Colour.dark_magenta(), url="https://www.fudstop.io")

        em.add_field(name="AH", value="```py\nDisplays After Hours Data for a ticker.```\n</dd ah:1004263746090324066>")
        em.add_field(name="Analyst", value="```py\nReturns analyst ratings for a ticker.```\n</dd analyst:1004263746090324066>")
        em.add_field(name="Bio", value="```py\nReturns the stock company's profile.```\n</dd bio:1004263746090324066>")
        em.add_field(name="Customer", value="```py\nDisplays customers of a company.```\n</dd customer:1004263746090324066>")
        em.add_field(name="ermove", value="```py\nDisplays implied move for a ticker based on option prices.```\n</dd ermove:1004263746090324066>")
        em.add_field(name="divinfo", value="```py\nDisplays dividend information for a ticker.```\n</dd divinfo:1004263746090324066>")
        em.add_field(name="earnings", value="```py\nPick a date and return the earnings scheduled for that day.```\n</dd earnings:1004263746090324066>")
        em.add_field(name="pm", value="```py\nDisplay premarket data for a stock.```\n</dd pm:1004263746090324066>")
        em.add_field(name="pt", value="```py\nDisplays a chart with price targets```\n</dd pt:1004263746090324066>")
        em.add_field(name="ytd", value="```py\nDisplays period performance for a stock.```\n</dd ytd:1004263746090324066>")
        em.add_field(name="sec", value="```py\nDisplays recent SEC filings.```\n</dd sec:1004263746090324066>")
        em.add_field(name="est", value="```py\nDisplays earnings estimates.```\n</dd est:1004263746090324066>")

        




        try:
            self.add_item(select11)
        except ValueError:
            self.clear_items()
            self.add_item(select11)

        
        select11.callback = lambda interaction: interaction.response.edit_message(view=MasterCommand())


        await inter.response.edit_message(embed=em, view=self)


class MasterPersistentViewBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned)
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            # Register the persistent view for listening here.
            # Note that this does not send the view to any message.
            # In order to do this you need to first send a message with the View, which is shown below.
            # If you have the message_id you can also pass it as a keyword argument, but for this example
            # we don't have one.
            self.add_view(MasterCommand())
            self.add_view(MasterView())
            self.add_view(PersistentView())
            self.persistent_views_added = True

        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")




me = MasterPersistentViewBot()

@me.command()
@commands.is_owner()
async def prepare(ctx: commands.Context):
    """Starts a persistent view."""
    # In order for a persistent view to be listened to, it needs to be sent to an actual message.
    # Call this method once just to store it somewhere.
    # In a more complicated program you might fetch the message_id from a database for use later.
    # However this is outside of the scope of this simple example.
    await ctx.send("```py\nSelect a category and the channels will print out for you!```", view=PersistentView())

@me.slash_command()
async def cmds(inter:disnake.AppCmdInter):
    view=disnake.ui.View()
    view.add_item(MasterDrop())
    await inter.send(view=view)

@me.command()
@commands.is_owner()
async def preparecommands(ctx: commands.Context):
    """Starts a persistent view."""
    # In order for a persistent view to be listened to, it needs to be sent to an actual message.
    # Call this method once just to store it somewhere.
    # In a more complicated program you might fetch the message_id from a database for use later.
    # However this is outside of the scope of this simple example.
    await ctx.send(view=MasterCommand())
#me.run("MTAxNjAwNjI5MzU5ODc2OTIwMg.GztNZZ.5GnsEeZixqJZ2RuzooA_FdnyAVoB3xaNmVnEhs")
