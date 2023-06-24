from disnake.ext import commands
import requests
import pandas as pd
import disnake
from _discord.views.menus import AlertMenus

class OFR(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.slash_command()
    async def ofr(self, inter):
        pass


    @ofr.sub_command()
    async def advanced_repo(self, inter:disnake.AppCmdInter):
        """View repo by participant! Updates Monthly"""
        await inter.response.defer()
        r = requests.get("https://www.financialresearch.gov/money-market-funds/data/portfolio_risks/data.json").json()

        datatable = r['datatable']
        highcharts = r['highcharts']

        name = [i['name'] if 'name' in i else None for i in highcharts]
        data = [i['data'] if 'data' in i else None for i in highcharts]
        for i in name:
            print(i)

        # Assume that columns and values are lists
        columns = [col_dict['title'] for col_dict in datatable['columns']]
        values = datatable['values']

        name_list = [
            'Aquila Investment Management ', 'Alger Funds', 'Sentinel Asset Management', 'EquiTrust Life Insurance Company', 'Timothy Plan',
            'Natixis Asset Management', 'Advanced Asset Management', 'Madison Mosaic', 'Direxion Funds', 'Semper Capital Management',
            'Scout Investments, Inc.', 'Selected Funds', 'Saratoga Capital  Management', 'Value Line', 'TCW Investment Management',
            'Bishop Street Capital', 'Old Mutual Capital', 'JNF Advisors Inc', 'RMB Asset Management', 'Pyxis Funds',
            'Ambassador Funds', 'Madison Investment', 'Nicholas Funds', 'Trust for Credit Unions', 'Russell', 'TCG Financial Services',
            'Weitz Investment Management', 'US Global Investors', 'Milestone', 'Eaton Vance', 'OneAmerica Funds',
            'Shelton Capital Management', 'Forward Funds', 'Alpine', 'Pacific Capital Investments', 'Performance Funds',
            'Ohio National Investments', 'Sun Life Financial', 'First Investors Management', 'Macquarie', 'Harbor',
            'Securian Financial', 'RS Funds', 'Penn Mutual Life', 'Sterling Capital', 'Mutual of America', 'ProFunds',
            'Homestead', 'Davis Funds', 'Hancock Horizon', 'Pacific Life', 'Calvert', 'RBB Fund', 'State Farm',
            'Williams Capital Management', 'CLS AdvisorOne', 'Miles Capital', 'Meeder Funds', 'Pioneer Investments',
            'Victory Capital Management', 'Touchstone', 'GE Asset Management', 'Paydenfunds', 'Northwestern Mutual',
            'Valic', 'William Blair', 'Huntington', 'SunAmerica', 'Virtus', 'Mass Mutual', 'Hartford Mutual Funds',
            'Lord Abbett', 'Allianz', 'Glenmede', 'Fifth Third', 'Guggenheim Investments', 'Lincoln National', 'Highmark',
            'Great-West Funds', 'Plan Investment Fund', 'American Beacon', 'PIMCO', 'Janus', 'AXA Equitable',
            'Bank of New York Mellon', 'GuideStone Funds', 'MainStay Funds', 'Ivy Funds', 'Transamerica', 'Voya',
            'Thrivent Financial', 'Gabelli Funds', 'Brown Brothers Harriman', 'Principal Funds', 'Putnam', 'Mount Vernon',
            'Nationwide', 'Cavanal Hill', 'Reich & Tang', 'Public Financial Management', 'John Hancock', 'BMO Funds',
            'TD Asset Management', 'Jackson National', 'CNI Charter', 'American Century', 'PNC Investments',
            'MFS Investment', 'Oppenheimer', 'USAA', 'Wilmington Funds', 'AllianceBernstein', 'TIAA-CREF',
            'SEI Investments', 'Columbia', 'Royal Bank of Canada', 'Dimensional', 'Franklin Templeton',
            'Bank of America', 'HSBC', 'Prudential', 'DWS Investments', 'T. Rowe Price', 'UBS', 'First American',
            'American Funds', 'Invesco', 'Legg Mason', 'Northern Trust Funds', 'State Street', 'Allspring Funds',
            'Morgan Stanley', 'Schwab', 'Dreyfus', 'Goldman Sachs', 'Federated', 'Blackrock', 'JP Morgan', 'Vanguard', 'Fidelity'
        ]

        reversed_name_list = name_list[::1]
        data_table = pd.DataFrame(values, columns=columns)
        data_table = data_table[::-1]
        filename = 'files/ofr/repo/repo_by_participants.csv'
        data_table.to_csv(filename)
        embeds = []
        for i,row in data_table.iterrows():
            date = row['Date']
            AquilaInvestmentManagement = row['Aquila Investment Management ']
            AlgerFunds = row['Alger Funds']
            SentinelAssetManagement = row['Sentinel Asset Management']
            EquiTrustLifeInsuranceCompany = row['EquiTrust Life Insurance Company']
            TimothyPlan = row['Timothy Plan']
            NatixisAssetManagement = row['Natixis Asset Management']
            AdvancedAssetManagement = row['Advanced Asset Management']
            MadisonMosaic = row['Madison Mosaic']
            DirexionFunds = row['Direxion Funds']
            SemperCapitalManagement = row['Semper Capital Management']
            ScoutInvestmentsInc = row['Scout Investments, Inc.']
            SelectedFunds = row['Selected Funds']
            SaratogaCapitalManagement = row['Saratoga Capital  Management']
            ValueLine = row['Value Line']
            TCWInvestmentManagement = row['TCW Investment Management']
            BishopStreetCapital = row['Bishop Street Capital']
            OldMutualCapital = row['Old Mutual Capital']
            JNFAdvisorsInc = row['JNF Advisors Inc']
            RMBAssetManagement = row['RMB Asset Management']
            PyxisFunds = row['Pyxis Funds']
            AmbassadorFunds = row['Ambassador Funds']
            MadisonInvestment = row['Madison Investment']
            NicholasFunds = row['Nicholas Funds']
            TrustforCreditUnions = row['Trust for Credit Unions']
            Russell = row['Russell']
            TCGFinancialServices = row['TCG Financial Services']
            WeitzInvestmentManagement = row['Weitz Investment Management']
            USGlobalInvestors = row['US Global Investors']
            Milestone = row['Milestone']
            EatonVance = row['Eaton Vance']
            OneAmericaFunds = row['OneAmerica Funds']
            SheltonCapitalManagement = row['Shelton Capital Management']
            ForwardFunds = row['Forward Funds']
            Alpine = row['Alpine']
            PacificCapitalInvestments = row['Pacific Capital Investments']
            PerformanceFunds = row['Performance Funds']
            OhioNationalInvestments = row['Ohio National Investments']
            SunLifeFinancial = row['Sun Life Financial']
            FirstInvestorsManagement = row['First Investors Management']
            Macquarie = row['Macquarie']
            Harbor = row['Harbor']
            SecurianFinancial = row['Securian Financial']
            RSFunds = row['RS Funds']
            PennMutualLife = row['Penn Mutual Life']
            SterlingCapital = row['Sterling Capital']
            MutualofAmerica = row['Mutual of America']
            ProFunds = row['ProFunds']
            Homestead = row['Homestead']
            DavisFunds = row['Davis Funds']
            HancockHorizon = row['Hancock Horizon']
            PacificLife = row['Pacific Life']
            Calvert = row['Calvert']
            RBBFund = row['RBB Fund']
            StateFarm = row['State Farm']
            WilliamsCapitalManagement = row['Williams Capital Management']
            CLSAdvisorOne = row['CLS AdvisorOne']
            MilesCapital = row['Miles Capital']
            MeederFunds = row['Meeder Funds']
            PioneerInvestments = row['Pioneer Investments']
            VictoryCapitalManagement = row['Victory Capital Management']
            Touchstone = row['Touchstone']
            GEAssetManagement = row['GE Asset Management']
            Paydenfunds = row['Paydenfunds']
            NorthwesternMutual = row['Northwestern Mutual']
            Valic = row['Valic']
            WilliamBlair = row['William Blair']
            Huntington = row['Huntington']
            SunAmerica = row['SunAmerica']
            Virtus = row['Virtus']
            MassMutual = row['Mass Mutual']
            HartfordMutualFunds = row['Hartford Mutual Funds']
            LordAbbett = row['Lord Abbett']
            Allianz = row['Allianz']
            Glenmede = row['Glenmede']
            FifthThird = row['Fifth Third']
            GuggenheimInvestments = row['Guggenheim Investments']
            LincolnNational = row['Lincoln National']
            Highmark = row['Highmark']
            GreatWestFunds = row['Great-West Funds']
            PlanInvestmentFund = row['Plan Investment Fund']
            AmericanBeacon = row['American Beacon']
            PIMCO = row['PIMCO']
            Janus = row['Janus']
            AXAEquitable = row['AXA Equitable']
            BankofNewYorkMellon = row['Bank of New York Mellon']
            GuideStoneFunds = row['GuideStone Funds']
            MainStayFunds = row['MainStay Funds']
            IvyFunds = row['Ivy Funds']
            Transamerica = row['Transamerica']
            Voya = row['Voya']
            ThriventFinancial = row['Thrivent Financial']
            GabelliFunds = row['Gabelli Funds']
            BrownBrothersHarriman = row['Brown Brothers Harriman']
            PrincipalFunds = row['Principal Funds']
            Putnam = row['Putnam']
            MountVernon = row['Mount Vernon']
            Nationwide = row['Nationwide']
            CavanalHill = row['Cavanal Hill']
            ReichTang = row['Reich & Tang']
            PublicFinancialManagement = row['Public Financial Management']
            JohnHancock = row['John Hancock']
            BMOFunds = row['BMO Funds']
            TDAssetManagement = row['TD Asset Management']
            JacksonNational = row['Jackson National']
            CNICharter = row['CNI Charter']
            AmericanCentury = row['American Century']
            PNCInvestments = row['PNC Investments']
            MFSInvestment = row['MFS Investment']
            Oppenheimer = row['Oppenheimer']
            USAA = row['USAA']
            WilmingtonFunds = row['Wilmington Funds']
            AllianceBernstein = row['AllianceBernstein']
            TIAACREF = row['TIAA-CREF']
            SEIInvestments = row['SEI Investments']
            Columbia = row['Columbia']
            RoyalBankofCanada = row['Royal Bank of Canada']
            Dimensional = row['Dimensional']
            FranklinTempleton = row['Franklin Templeton']
            BankofAmerica = row['Bank of America']
            HSBC = row['HSBC']
            Prudential = row['Prudential']
            DWSInvestments = row['DWS Investments']
            TRowePrice = row['T. Rowe Price']
            UBS = row['UBS']
            FirstAmerican = row['First American']
            AmericanFunds = row['American Funds']
            Invesco = row['Invesco']
            LeggMason = row['Legg Mason']
            NorthernTrustFunds = row['Northern Trust Funds']
            StateStreet = row['State Street']
            AllspringFunds = row['Allspring Funds']
            MorganStanley = row['Morgan Stanley']
            Schwab = row['Schwab']
            Dreyfus = row['Dreyfus']
            GoldmanSachs = row['Goldman Sachs']
            Federated = row['Federated']
            Blackrock = row['Blackrock']
            JPMorgan = row['JP Morgan']
            Vanguard = row['Vanguard']
            Fidelity = row['Fidelity']
            embed = disnake.Embed(title="Reverse Repo by Participant", description=f"```py\n{date}```")
            for i in range(0, len(reversed_name_list), 25):
                names_batch = name_list[i:i+25]
                for name in names_batch:
                    embed.add_field(name=name, value=row[name], inline=False)
                    embeds.append(embed)
        view = AlertMenus(embeds)

        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(filename))

        
        view.add_item(button)
  

        await inter.edit_original_message(embed=embeds[0], view=view)
async def setup(bot:commands.Bot):
    await bot.add_cog(OFR(bot))
    print(f"> Extension {__name__} is ready\n")