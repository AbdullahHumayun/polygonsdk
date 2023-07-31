import disnake
from disnake.ext import commands
from disnake import Option, OptionType, OptionChoice

from views.learnviews import MenuStart,AlertStart, DiscordStart,TAStart,MarketsView,CryptoViewStart,PageTwoView,PageThreeView,HighShortsViewStart,LowFloatDropdown
from views.learnviews import ForexViewStart,FTDViewStart,LosersViewStart,GainersViewStart,ActiveViewStart
from views.learnviews import TotalOIViewStart,TotalVolumeViewStart
from views.learnviews import CoreStart, LinksStartView,LitStart,DataViewStart
from views.learnviews import WebullCmdViewStart,DDCmdViewStart,OptionCmdViewStart,FlowCmdViewStart,DPSCmdViewStart,EarningsCmdViewStart,EconomyCmdViewStart,LearnCmdViewStart,StreamCmdViewStart,StockCmdViewStart,ChartingCmdViewStart
from views.learnviews import HelpStart,VideoStartView,VideoStart2View,VideoStart3View,TopOptionsViewStart, AgencyViewStart
from views.learnviews import DTCCViewStart,NYSEViewStart, CBOEViewStart, OFRDataViewStart
from views.learnviews import TopOIDownViewStart,TopOIUpViewStart,TopIVViewStart,TopOIViewStart,TopVolumeViewStart,TotalTurnoverViewStart,TotalOIViewStart,TotalVolumeViewStart
from views.learnviews import FedDataStart,FINRADataStart,BlockchainDataStart,InflationDataStart,EconomicDataStart,TreasuryDataStart,HKEXDataStart,MMFDataStart,RepoDataStart
from views.learnviews import StockPage1,StockPage2,StockPage3,StockPage4,StockPage5, AppStart, ToolsViewStart
from views.learnviews import OFRViewStart, RepoCitedViewStart,CriteriaView,CommandsStart,PermaFTDViewStart, AvoidView, AlertMenus, ServerMenuView

from sdks.polygon_sdk.list_sets import subscriptions as subs
role_dict = {
'os🐂day🐂rsi':'1134938376789827687',
'nyse🏛arca':'1134934887191810050',
'basic🌱materials':'1134934885891575918',
'scalps🔮':'1134934883744092200',
'real🏢estate':'1134934881512726578',
'rss🔊mad_money':'1134934879415570493',
'50k➖100k':'1134934877301645442',
'bankrupt📛delinquent':'1134934874034286703',
'corrected🔐close':'1134934872423682199',
'avg🍢price🍢trade':'1134934870905340054',
'upside💫hour⏫':'1134934869382795284',
'cv📜papers_works':'1134934867730251867',
'insider🔮trades':'1134934863410114580',
'downside💫hour⏬':'1134934861728198811',
'cv📜core':'1134934859882713149',
'below⏬avg⏬vol':'1134934858213371934',
'cboe_bzx':'1134934854916644965',
'cons🛡defensive':'1134934851498295329',
'odd🍢lot':'1134934849522765915',
'below📛req':'1134934844313444363',
'nasdaq_bx':'1134934843092901979',
'rss🔊sec':'1134934841524240494',
'cv📜psychology':'1134934839536136232',
'form🪥t':'1134934838189772840',
'trade🐉thru🐉exempt':'1134934836369436762',
'long🩹appendage':'1134934834171625634',
'cancelled🦜':'1134934832292565082',
'utilities💡':'1134934830476427325',
'os🐂hour🐂rsi':'1134934828731609148',
'short💉appendage':'1134934826844168284',
'closing📪prints':'1134934824419860562',
'multi🦜vs🦜single':'1134934821433520199',
'ise🏛':'1134934819390881906',
'multi🦜floor':'1134934815595057372',
'above⏫avg⏫vol':'1134934813443358861',
'btc🪙':'1134934811748868147',
'bullseye🔮':'1134934809974685757',
'nyse🏛chicago':'1134934808284368897',
'golden🔮sweeps':'1134934806279508029',
'financial💰services':'1134934803456725092',
'crypto📰forex':'1134934801514762252',
'single🦜cross':'1134934800109674577',
'industrials🏭':'1134934798352269423',
'rss🔊yahoo':'1134934796670349403',
'near🔻52🔻low':'1134934793847591055',
'fd📶unusual':'1134934791377145977',
'nasdaq_mrx':'1134934789716181032',
'energy⚡':'1134934783315685486',
'🗣announcements':'1134934781310804068',
'penny':'1134934778479640616',
'super🐻overbought':'1134934776399265892',
'cv📜macro':'1134934773039644732',
'super🐂oversold':'1134934771449987172',
'ob🐻week🐻rsi':'1134934767922598069',
'1k➖5k':'1134934763862499329',
'ob🐻hour🐻rsi':'1134934762306416822',
'communication📞':'1134934754299490314',
'late📛filing':'1134934746284163132',
'darkpool🔮':'1134934744853921842',
'miax🏛pearl':'1134934742366699601',
'spx🌲calls':'1134934740227596328',
'multi🦜auction':'1134934737501294633',
'canceled':'1134934735773245521',
'cboe_c2':'1134934726738714796',
'nasdaq_philly':'1134934722724778146',
'near🔺52🔺high':'1134934720887664772',
'zero⭕dte':'1134934719205756989',
'ise':'1134934717599334562',
'healthcare🏥':'1134934712570359899',
'cboe':'1134934705943359589',
'🤖command_room':'1134934704093659307',
'🦹♂wait_here🦹♂':'1134934697147900096',
'cv📜trading':'1134934693368832060',
'official🔒close':'1134934691439456386',
'next⏭day':'1134934685626150953',
'downside💫day⏬':'1134934684359479378',
'nyse_arca':'1134934682824364134',
'spy🔻puts':'1134934678109945906',
'nbbo🔢quotes':'1134934675928924160',
'cboe🏛edga':'1134934674175705200',
'cv📜debunks':'1134934672544112791',
'nyse_american':'1134934668786012301',
'rss🔊cnbc':'1134934664931459143',
'auto🦜execution':'1134934662800756897',
'introduction🐍':'1134934660829425734',
'500➖1k':'1134934659168485516',
'vwap💹stocks':'1134934657343963227',
'prior🍢reference':'1134934653501964288',
'only🦜canceled':'1134934651618730135',
'1k-5k':'1134934647810293801',
'nyse🏛american':'1134934644165447775',
'miax_pearl':'1134934642571612170',
'cboe_edgx':'1134934636745728123',
'accumulation🚀':'1134934631246987316',
'opening📫prints':'1134934629565087875',
'miax':'1134934627761541171',
'financially🩸deficient':'1134934626008309880',
'sell🩸specials':'1134934624380932146',
'breakouts🔮':'1134934622325710909',
'multi🦜cross':'1134934620815769721',
'iso🦜auction':'1134934618982846536',
'nasdaq🏛':'1134934615388344320',
'intermarket🧹sweep':'1134934611298897970',
'rss🔊marketbeat':'1134934609482752050',
'cboe🏛edgx':'1134934607939248199',
'5k-10k':'1134934606047617197',
'500-1k':'1134934604726419536',
'floor🦜trade':'1134934602876715161',
'cv📜sec-filings':'1134934600989298791',
'cv📜china':'1134934599307362384',
'nasdaq🏛philly':'1134934596828528771',
'earnings💰today':'1134934594995626044',
'cv📜research':'1134934592869126215',
'ob🐻minute🐻rsi':'1134934590096674867',
'20k➖50k':'1134934586871267458',
'🆕fifty_low':'1134934584585367632',
'cboe🏛bzx':'1134934582827950130',
'rss🔊nscc':'1134934580286193769',
'option🤖auto🤖trade':'1134934576553267200',
'upside💫day⏫':'1134934574510653551',
'investors🏛exchange':'1134934572635795546',
'etfs⚓':'1134934571243290674',
'10k➕':'1134934569678819400',
'analyst🔮grades':'1134934568076582972',
'ob🐻day🐻rsi':'1134934566612779179',
'contingent🪃qualified':'1134934564461088863',
'unusual💥options':'1134934560677838951',
'fd📶opening_flow':'1134934557691478046',
'fire🔥sale':'1134934554944213023',
'cv📜analysis':'1134934553757237358',
'rss🔊dtcc':'1134934552519909526',
'cv📜history':'1134934550951231619',
'cons🎢cyclical':'1134934548505972787',
'boston_eexchange':'1134934544651407511',
'ch💬main_chat': '1134981157289742418',
'redempt🚫suspension':'1134934542726205590',
'ch💬jasmy🇯🇵': '1134976422901989488',
'contingent🪃':'1134934540893290616',
'ta📈technicals':'1134934539328819282',
'ch💬profit_loss💸': '1134976311815839794',
'code🐍snippets':'1134934537911152691',
'100k➕':'1134934535147094187',
'finra🏛adf':'1134934533611991122',
'option🔮sweeps':'1134934529811959909',
'fd📶buys_sells':'1134934528092278784',
'rss🔊nytimes':'1134934525164650586',
'data🐍structures':'1134934523218493521',
'multi🦜proprietary':'1134934521222004747',
'multi🦜electronic':'1134934518889980075',
'cboe🏛byx':'1134934516746686495',
'squeeze💦potential':'1134934515291262987',
'members🏛exchange':'1134934513194106880',
'xrp🪙':'1134934511805804755',
'retail🐐bid🐐ask':'1134934510010646630',
'miax_emerald':'1134934507368239194',
'eth🪙':'1134934500237910118',
'spx🔻puts':'1134934498849587281',
'technology💻':'1134934497134121001',
'discord🐍bot':'1134934494110036128',
'retail🐂ask':'1134934492432310323',
'spy🌲calls':'1134934490536497183',
'nasdaq_global':'1134934486413475860',
'nyse🏛':'1134934480717627402',
'ai🔮news':'1134934478805020762',
'🧹sweeps':'1134934476116459591',
'earnings💰week':'1134934474325508096',
'nadaq🏛omx':'1134934470194114741',
'os🐂week🐂rsi':'1134934468654801018',
'auto🦜vs🦜single':'1134934466914160710',
'🆕52_high':'1134934463852335196',
'crypto🔮signals':'1134934461889380373',
'single🦜auction':'1134934458882076743',
'os🐂minute🐂rsi':'1134934457091108915',
'option🦜auction':'1134934453400125550',
'jasmy🪙':'1134934451621736469',
'vwap��ooptions':'1134934449298079846',
'fd📶goldensweep':'1134934446991224942',
'rss🔊finra':'1134934444101341294'}
channel_dict = {'rss🔊finra': 1019360302250332301,'fd📶goldensweep': 1089364481672478780, 'vwap��ooptions': 1130895690315345920, 'jasmy🪙': 1132077557605482566,'option🦜auction': 1133412240331112448, 'earnings📰dividends': 1130687470028214284, 'os🐂minute🐂rsi': 1124185351477526539, 'single🦜auction': 1113149881352192030, 'us🌐dollar': 1132051150061977670, 'crypto🔮signals': 1112768289303711945, '🆕52_high': 1129889515100721383, 'volatility🌐': 1131796600784695446, 'auto🦜vs🦜single': 1129489372698378321, 'os🐂week🐂rsi': 1131240086378393600, 'nadaq🏛omx': 1129100013784539187, 'ch💬main_chat': 896207280117264434, 'earnings💰week': 1129909147157155840, '🧹sweeps': 1113143417334157332, 'ai🔮news': 1112740350059098162, 'nyse🏛': 1127437282836758589, 'Indices🌐': 1131781952249270375, 'nasdaq_global': 1127644705635713136,'technology🌐': 1132074237008548002, 'spy🌲calls': 1133428070649450516, 'retail🐂ask': 1130552915866681425, 'discord🐍bot': 1093754744872378408, 'econ📰indicators': 1130687882143735868, 'technology💻': 1113677893537632316, 'spx🔻puts': 1133418198209933402,'eth🪙': 1132077554774319154, 'ch💬offtopic⬅': 943359218545721395, 'retail🐻bid': 11305480095067902032, 'miax_emerald': 1127644702078939276, 'retail🐐bid🐐ask': 1130552893896933376, 'xrp🪙': 1132077537523146923, 'members🏛exchange': 1127443940107358269, 'squeeze💦potential': 1129908107447906364, 'cboe🏛byx': 1127444925370335252, 'multi🦜electronic': 1129489929773260872, 'multi🦜proprietary': 1134554830627672135, 'data🐍structures': 1093378561982857316, 'rss🔊nytimes': 1053789818007584938, 'bitstamp👛': 1132026720250249336, 'fd📶buys_sells': 1089364148535701544, 'option🔮sweeps': 1112755644357947523, 'basic🌐materials': 1132073649512382564, 'finra🏛adf': 1127437139664191588,'100k➕': 1129958843003179069, 'market📰regions': 1130687562239975505, 'code🐍snippets': 1094116008685482034,'ta📈technicals': 1052110396280021022, 'contingent🪃': 1133415980152922233, 'redempt🚫suspension': 1130602916223398020, 'boston_eexchange': 1127645868670070895, 'short🌐': 1131809474483601518,'cons🎢cyclical': 1113676873495482451,'cv📜history': 1050988130947313744, 'rss🔊dtcc': 1028667813168173167, 'cv📜analysis': 1051164194365509643, 'fire🔥sale': 1129773962319102042, 'fd📶opening_flow': 1035273203683172434, 'rules': 1091613553670238229, 'unusual💥options': 1134562800270844014, 'analyst📰ratings': 1130688025375019070, 'contingent🪃qualified': 1133415730939973752, 'ob🐻day🐻rsi': 1131238733790851122, 'analyst🔮grades': 1112768500923109416,  '10k➕': 1129768558126170212,  'etfs⚓': 1113677417182146560, 'investors🏛exchange': 1127443966430818344, 'upside�dday⏫': 1113563471141941420, 'option🤖auto🤖trade': 1129905458480689242, 'stocks📰': 1130687104322654248, 'rss🔊nscc': 1028668345702166698, 'cboe🏛bzx': 1127437289212084335, '🆕fifty_low': 1129889517210447882, '20k➖50k': 1129958790305951885, 'spx🌐dispersion': 1131805729079169114, 'ob🐻minute🐻rsi': 1124185353486602331,'mkt📰sentiments': 1130688165489942658, 'cv📜research': 1051162433768656916, 'earnings💰today': 1129773964122665001, 'nasdaq🏛philly': 1134470593983557693, 'cv📜china': 1051162308145057802, 'cv📜sec-filings': 1050979909780111360, 'floor🦜trade': 1129885678063337474,'500-1k': 1129768539402813470, '5k-10k': 1129768556461043832,'cboe🏛edgx': 1127444335563112508, 'rss🔊marketbeat': 1053789985909768254,'intermarket🧹sweep': 
 1126246919732199454, 'fin📰services': 1130687790418497536, 'nasdaq🏛': 1127437290801733732, 'skews🌐': 1131796602365952000, 'iso🦜auction': 1133412527406059600, 'multi🦜cross': 1133426263546134568, 'breakouts🔮': 1112740590845702305, 'sell🩸specials': 1088507701727866982, 'financially🩸deficient': 1129790144073973860, 'miax': 1127644694764068946, 'opening📫prints': 1127432812891484241, 'accumulation🚀': 1129773960641392720, 'futures🌐': 1131808463283040386, 'spoons-of-investing': 947504895454507008, 'cboe_edgx': 1127648686537715812, 'Momentum💫Scalps': 1113438888862695476, 'miax_pearl': 1127645866463871036, 'nyse🏛american': 1127437292223598695,'1k-5k': 1129768554326151179, 'only🦜canceled': 1133451695985266738,'prior🍢reference': 1129843316830257152, 'news📰events': 1130687608247291955, 'vwap💹stocks': 1130895687601619034, '500➖1k': 1129957924710654042, 'introduction🐍': 1093363122678534274, 'auto🦜execution': 1133411763749142548, 'rss🔊cnbc': 1053789646926123086, 'investor📰rel': 1130687424704548884, 'nyse_american': 1127646980202578000, 'offers📰': 1130688072300908554, 'cv📜markets': 10511622494904844308, 'cv📜debunks': 1051563232642474025,  'cboe🏛edga': 1127445656835993680, 'nbbo🔢quotes': 1133150168133419109, 'spy🔻puts': 1133428072411058279, 'sector📰stocks': 1130687378797899796,'ch💬paper-trading': 1006354207294627952, 'nyse_arca': 1127646519089184878, 'downside💫day⏬': 1113563469787176960, 'next⏭day': 1129787726254841899, 'official🔒close': 1129908108773310614, 'cv📜trading': 1051162176850763806, 'cloud🌐': 1131806057153445889, '🦹♂wait_here🦹♂': 1134906474972323993, 'fm❓questions': 1019642125442363483, 'coinbase👛': 1132026196071305266, 'filecoin🌐': 1131782176711651438,'🤖command_room': 1015631772660269156, 'cboe': 1127644699541381261, 'bitfinex👛': 1132026539203100862, 'healthcare🏥': 1113677301079613541, 'corp📰news': 1130687287466917978, 'industrials🌐': 1132074266184138772, 'ise': 1127644696991256596, 'zero⭕dte': 1134556646278975599, 'near🔺52🔺high': 1129889300536889425, 'nasdaq_philly': 1127647928580845658, 'china🌐': 1131796765050425375, 'cboe_c2': 1127649018978258994, 'benchmark🌐': 1131806933377101934, 'canceled': 1133441628179275888, 'multi🦜auction': 1113146480455331840, 'spx🌲calls': 1133417838745501796, 'miax🏛pearl': 1127444927215849564, 'darkpool🔮': 1112755591358722199,'late📛filing': 1134233920309821551, 'market📰analysis': 1130687654246223883,'communication📞': 1113677732786753566, 'etfs📰': 1130687196404383856, 'legal📰info': 1130687516824043550, 'ch💬commands': 1121659548915204117, 'ob🐻hour🐻rsi': 1131238731421065216, '1k➖5k': 1129958170685612072, 'kraken👛': 1132025944379506728, 'ob🐻week🐻rsi': 1131240110957023342, 'market📰news': 1130687242097131614,'super🐂oversold': 1131242629573644348, 'cv📜macro': 1051162285353218119, 'uncon📰invest': 1130687928566296606, 'super🐻overbought': 1131242627690401942,'penny': 1037716097039867904, '🗣announcements': 1018395415579742300,'energy⚡': 1113677585881239622,  'industry📰news': 1130687835779911680, 'investing📰edu': 1130687333268738088, 'nasdaq_mrx': 1127646516711018506, 'fd📶unusual': 1089364318274990191, 'near🔻52🔻low': 1129889302365605980,'rss🔊yahoo': 1053789896352993341, 'industrials🏭': 1113677389973704735, 'single🦜cross': 1133417470363971794, 'crypto📰forex': 1130687699599237260, 'financial💰services': 1113677818925158400, 'golden🔮sweeps': 1112768180469891255, 'nyse🏛chicago': 1129099480747233300, 'bullseye🔮': 1112740518753996851, 'btc🪙': 1132077552467456170, 'above⏫avg⏫vol': 1129172144430006272, 'multi🦜floor': 1113144168567537795, 'ch💬jasmy🇯🇵': 1134976422901989488, 'ise🏛': 1129160457463267509, 'multi🦜vs🦜single': 1113147180140728383, 'penny📰stocks': 1130687150699065404, 'closing📪prints': 1127431885765746699,'short💉appendage': 1130616468015419404, 'os🐂hour🐂rsi': 1131238729298759750, 'utilities💡': 1113677583662456883, 'cancelled🦜': 1133438997734096926, 'long🩹appendage': 1130616533069086891, 'trade🐉thru🐉exempt': 1130652311237169193,'form🪥t': 1130652444494409778, 'cv📜psychology': 1051162149084467250, 'rss🔊sec': 1019360339856470146, 'nasdaq_bx': 1127644703869906974, 'below📛req': 1134233637353693355, 'product📰announce': 1130687974477148220, 'odd🍢lot': 1127382010403496089, 'cons🛡defensive': 1113677020178694155, 'fed📰news': 1130687745111625749, 'cboe_bzx': 1127645871819989184, 'ch💬profit_loss💸': 1134976311815839794, 'below⏬avg⏬vol': 1129172165867081818, 'cv📜core': 1051167628858753085, 'downside💫hour⏬': 1113439375179644979, 'insider🔮trades': 1112768636961181717, 'cv📜papers_works': 1051584539358658580,'upside💫hour⏫': 1113439351246946415, 'ssr🪃': 11126351105832521738, 'avg🍢price🍢trade': 1133413982930219048, 'corrected🔐close': 1129789578186854483,'bankrupt📛delinquent': 1134233104618373281, 'ronald': 960215402779132015, '50k➖100k': 1129958820173590548,'rss🔊mad_money': 1042559047896932362, 'real🏢estate': 1113677158854971403, 'scalps🔮': 1112768263911387157,'basic🌱materials': 1113677536245862420, 'nyse🏛arca': 1127438589446336592,'ch💬hangout': 1134976186825576538,'os🐂day🐂rsi': 1131238736353562745, 'ch💬main_chat': 1134976042474426489}


REQUIRED_ROLES = [
    '1002249878283493456',
    '938824920589283348',
    '1086118401660964917',
    '1086118401660964916',
    '941029523699400705',
    '896207245853999145'
]
intents=disnake.Intents.all()
class PersistentViewBot(commands.Bot):
    def __init__(self, command_prefix, intents, tickers=subs, embeds=str):
        self.ticker = tickers
        super().__init__(command_prefix=command_prefix, intents=disnake.Intents.all())
        self.persistent_views_added = False
        self.embeds = []

    async def on_ready(self):
        if not self.persistent_views_added:
            # Register the persistent view for listening here.
            # Note that this does not send the view to any message.
            # In order to do this you need to first send a message with the View, which is shown below.
            # If you have the message_id you can also pass it as a keyword argument, but for this example
            # we don't have one.
            self.add_view(AvoidView())
            self.add_view(PageTwoView())
            self.add_view(PageThreeView())
            self.add_view(CommandsStart())
            self.add_view(MenuStart())
            self.add_view(CoreStart())
            self.add_view(AlertStart())
            self.add_view(LitStart())
            self.add_view(DiscordStart())
            self.add_view(TAStart())
            self.add_view(MarketsView())
            self.add_view(CryptoViewStart())
            self.add_view(ForexViewStart())
            self.add_view(HighShortsViewStart())
            self.add_view(LowFloatDropdown())
            self.add_view(AlertMenus(embeds=self.embeds))
            self.add_view(FTDViewStart())
            self.add_view(LosersViewStart())
            self.add_view(GainersViewStart())
            self.add_view(ActiveViewStart())
            self.add_view(TotalOIViewStart())
            self.add_view(TotalVolumeViewStart())
            self.add_view(LinksStartView())
            self.add_view(AppStart())
            self.add_view(TopOptionsViewStart())
            self.add_view(WebullCmdViewStart())
            self.add_view(OptionCmdViewStart())
            self.add_view(PermaFTDViewStart())
            self.add_view(OFRViewStart())
            self.add_view(DDCmdViewStart())
            self.add_view(FlowCmdViewStart())
            self.add_view(DPSCmdViewStart())
            self.add_view(EconomyCmdViewStart())
            self.add_view(EarningsCmdViewStart())
            self.add_view(FlowCmdViewStart())
            self.add_view(StreamCmdViewStart())
            self.add_view(ChartingCmdViewStart())
            self.add_view(StockCmdViewStart())
            self.add_view(HelpStart())
            self.add_view(LearnCmdViewStart())
            self.add_view(ToolsViewStart())
            self.add_view(NYSEViewStart())
            self.add_view(DTCCViewStart())
            self.add_view(CBOEViewStart())
            self.add_view(StockPage1())
            self.add_view(StockPage2())
            self.add_view(StockPage3())
            self.add_view(StockPage4())
            self.add_view(StockPage5())
            self.add_view(TopIVViewStart())
            self.add_view(TopOIDownViewStart())
            self.add_view(TopOIUpViewStart())
            self.add_view(TotalTurnoverViewStart())
            self.add_view(TopVolumeViewStart())
            self.add_view(TopOIViewStart())
            self.add_view(VideoStartView())
            self.add_view(VideoStart3View())
            self.add_view(VideoStart2View())
            self.add_view(OFRDataViewStart())
            self.add_view(AgencyViewStart())
            self.add_view(DataViewStart())
            self.add_view(InflationDataStart())
            self.add_view(BlockchainDataStart())
            self.add_view(HKEXDataStart())
            self.add_view(FINRADataStart())
            self.add_view(MMFDataStart())
            self.add_view(FedDataStart())
            self.add_view(TreasuryDataStart())
            self.add_view(EconomicDataStart())
            self.add_view(RepoDataStart())
            self.add_view(RepoCitedViewStart())
            self.add_view(CriteriaView())
            self.add_view(AvoidView())
            self.add_view(ServerMenuView())
            self.add_view(ChannelsView())

            self.persistent_views_added = True


        print(f"Logged in as {self.user} (ID: {self.user.id})")


bot = PersistentViewBot(command_prefix=">>", intents=intents)



class ChannelsView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
        self.add_item(ChannelSelector())

class ChannelSelector(disnake.ui.ChannelSelect):
    def __init__(self):
        super().__init__(custom_id="channelSelector", placeholder="Select a Channel -->",min_values=1,max_values=25,channel_types=[disnake.ChannelType.text])



    async def callback(self, interaction: disnake.Interaction):

        member = interaction.user
        guild = interaction.guild
        # Debug: Print the IDs of the roles that the member has
        member_role_ids = [str(role.id) for role in member.roles]
        print("Member's role IDs:", member_role_ids)

        # Check if the member has any of the required roles
        has_required_role = any(str(role.id) in REQUIRED_ROLES for role in member.roles)

        # Debug: Print the result of the check
        print("Has required role:", has_required_role)
        # Check if the member has any of the required roles
        if any(str(role.id) in REQUIRED_ROLES for role in member.roles):
            # Get the selected channels
            selected_channels = self.values
            print(selected_channels)


            response_messages = []

            for channel in selected_channels:
                channel_name = channel.name
                role_id = role_dict.get(channel_name)

                if role_id:
                    role = disnake.utils.get(guild.roles, id=int(role_id))
                    if role:
                        await member.add_roles(role)
                        response_messages.append(f"Access granted to channel {channel_name}")
                    else:
                        response_messages.append(f"Role not found for channel {channel_name}")
                else:
                    response_messages.append(f"Role name not found for channel {channel_name}")

            final_response = '\n'.join(response_messages)
            await interaction.response.edit_message(final_response)