"""REDDIT SCRAPER"""
import disnake
import requests
from disnake.ext import commands
from requests.auth import HTTPBasicAuth

class Reddit(commands.Cog):
    """MAIN CLASS"""
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def reddit(self, interaction):
        """PARENT"""
        

    @reddit.sub_command()
    async def gme_go_brr(self,inter: disnake.AppCmdInter):
        """☔Lookup the GME GO BRR Poster"""
        await inter.response.defer(with_message=True)
        auth = HTTPBasicAuth('NMV_R9HR7oWtrYp20aDQxA', 'EvlxSIm8-9UkVXfITWS9L7mBATbo4g')


        data = {'grant_type': 'password',
                'username': 'YOUR REDDIT LOGIN',
                'password': 'YOUR REDDIT PASSWORD'}
        headers = {'User-Agent': 'YOUR REDDIT BOT'}


        res = requests.post('https://www.reddit.com/api/v1/access_token',
                            auth=auth, data=data, headers=headers)
        TOKEN = res.json()['access_token']
        headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

        requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

        res = requests.get("https://oauth.reddit.com/user/deepfuckingvalue/", #the guy's profile
                        headers=headers)

        data = res.json() #convert the data to .json format!

        datas = data['data'] #variable name 2
        #after = datas['after']
        #dist = datas['dist']
        #modhash = datas['modhash']
        #geo_filter = datas['geo_filter']
        children = datas['children']
        #before = datas['children']

        #print(children) #bingo
        itemb1 = children[0]
        data1 = itemb1['data']
        subreddit=data1['subreddit']
        #author_fullname=data1['author_fullname']
        #saved=data1['saved']
        mod_reason_title=data1['mod_reason_title']
        #gilded=data1['gilded']
        #clicked=data1['clicked']
        title=data1['title']
        #subreddit_name_prefixed=data1['subreddit_name_prefixed']
        #hidden=data1['hidden']
        #pwls=data1['pwls']
        #downs=data1['downs']
        #thumbnail_height=data1['thumbnail_height']
        top_awarded_type=data1['top_awarded_type']
        #hide_score=data1['hide_score']
        name=data1['name']
        #quarantine=data1['quarantine']
        upvote_ratio=data1['upvote_ratio']
        #ups=data1['ups']
        total_awards_received=data1['total_awards_received']
        #media_embbed=data1['media_embbed']
        #thumbnail_width=data1['thumbnail_width']
        #author_flair_tembplate_id=data1['author_flair_tembplate_id']
        is_original_content=data1['is_original_content']
        #user_reports=data1['user_reports']
        #secure_media=data1['secure_media']
        #is_reddit_media_domain=data1['is_reddit_media_domain']
        #is_meta=data1['is_meta']
        #category=data1['category']
        #secure_media_embbed=data1['secure_media_embbed']
        score=data1['score']
        approved_by=data1['approved_by']
        is_created_from_ads_ui=data1['is_created_from_ads_ui']
        #author_prembium=data1['author_prembium']
        thumbnail=data1['thumbnail']
        edited=data1['edited']
        #gildings=data1['gildings']
        #post_hint=data1['post_hint']
        #content_categories=data1['content_categories']
        #subreddit_type=data1['subreddit_type']
        created=data1['created']
        #link_flair_type=data1['link_flair_type']
        #wls=data1['wls']
        #remboved_by_category=data1['remboved_by_category']
        #banned_by=data1['banned_by']
        #author_flair_type=data1['author_flair_type']
        #domain=data1['domain']
        likes=data1['likes']
        #suggested_sort=data1['suggested_sort']
        #url_overridden_by_dest=data1['url_overridden_by_dest']
        #view_count=data1['view_count']
        #archived=data1['archived']
        #no_follow=data1['no_follow']
        #is_crosspostable=data1['is_crosspostable']
        #pinned=data1['pinned']
        #over_18=data1['over_18']
        #preview=data1['preview']
        #all_awardings=data1['all_awardings']
        #awarders=data1['awarders']
        #media_only=data1['media_only']
        #can_gild=data1['can_gild']
        #spoiler=data1['spoiler']
        #locked=data1['locked']
        #author_flair_text=data1['author_flair_text']
        #treatment_tags=data1['treatment_tags']
        #visited=data1['visited']
        #remboved_by=data1['remboved_by']
        #mod_note=data1['mod_note']
        #distinguished=data1['distinguished']
        #subreddit_id=data1['subreddit_id']
        author_is_blocked=data1['author_is_blocked']
        #mod_reason_by=data1['mod_reason_by']
        #num_reports=data1['num_reports']
        #remboval_reason=data1['remboval_reason']
        #link_flair_background_color=data1['link_flair_background_color']
        is_robot_indexable=data1['is_robot_indexable']
        #report_reasons=data1['report_reasons']
        author=data1['author']
        #discussion_type=data1['discussion_type']
        #num_comments=data1['num_comments']
        #send_replies=data1['send_replies']
        #whitelist_status=data1['whitelist_status']
        #contest_mode=data1['contest_mode']
        #mod_reports=data1['mod_reports']
        #permalink=data1['permalink']
        #parent_whitelist_status=data1['parent_whitelist_status']
        #stickied=data1['stickied']
        url=data1['url']
        subreddit_subscribers=data1['subreddit_subscribers']
        #created_utc=data1['created_utc']
        num_crossposts=data1['num_crossposts']
        #media=data1['media']
        #is_video=data1['is_video']
        emb = disnake.Embed(title=title, description=f"```py\n{subreddit}```", url=url)
        emb.add_field(name="Subreddit:", value=f"```py\n{subreddit}```")
        emb.add_field(name="Author is blocked?", value=f"```py\n{author_is_blocked}```")
        emb.add_field(name="Approved By:", value=f"```py\n{approved_by}```")
        emb.add_field(name="Is Original Content?", value=f"```py\n{is_original_content}```")
        emb.add_field(name="Total Awards Recieved:", value=f"```py\n{total_awards_received}```")
        emb.add_field(name="Top Awarded Type:", value=f"```py\n{top_awarded_type}```")
        emb.add_field(name="Likes:", value=f"```py\n{likes}```")
        emb.add_field(name="Is edited?", value=f"```py\n{edited}```")
        emb.add_field(name="Created from ads?", value=f"```py\n{is_created_from_ads_ui}```")
        emb.add_field(name="#of times crossposted:", value=f"```py\n{num_crossposts}```")
        emb.add_field(name="Score:", value=f"```py\n{score}```")
        emb.add_field(name="Upvote Ratio:", value=f"```py\n{upvote_ratio}```")
        emb.add_field(name="Is robot indexable?", value=f"```py\n{is_robot_indexable}```")
        emb.add_field(name="Post name:", value=f"```py\n{name}```")
        emb.add_field(name="Author:", value=f"```py\n{author}```")
        emb.add_field(name="{author}'s # of Followers:", value=f"```py\n{subreddit_subscribers}```")
        emb.set_image(url=thumbnail)
        emb.set_footer(text=f"Created at {created}")
        await inter.edit_original_message(embbed=emb)


def setup(bot):
    """REDDIT COG"""
    bot.add_cog(Reddit(bot))
    print(f"> Extension {__name__} is ready\n")
