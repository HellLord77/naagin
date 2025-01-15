import csv
import functools
import gzip
import hashlib
import json
import logging
import shutil
from csv import DictReader
from csv import DictWriter
from io import StringIO
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.algorithms import AES

import config
import utils

CSV_FILE_LISTS = {
    10: {
        "Beach_Flag_Data.csv": "639ba29bdf2cc0c2fcb562d8854fd9ba",
        "birthday.csv": "44fcf7d58abe9f0cef79e20adfa3b05a",
        "birthday_reward.csv": "618aceb2f2d56e527ff26c099b7118a1",
        "Blackjack_CharaParam.csv": "1d5cc66fcad4d05bb642794c858ee3fb",
        "CasinoExchange.csv": "3676eeb8110bd64d30d5d3aab11632c7",
        "CasinoGoldChipInfo.csv": "c289f95bbca797f631f11fb8cc11fb61",
        "CasinoTop.csv": "39a0ddf1b2f17ca9e2e62aff270933cb",
        "Consume_Parameter.csv": "206afa785bcc9ff78d10f331435da469",
        "ConteList.csv": "8ab596c740a714b516bce4cd30a6c5cf",
        "Costume_PullPoint.csv": "eef73e9775b09e394596b681a049745d",
        "CR_Birthday.csv": "7a7089441e096e0049b531c0196d2562",
        "CR_FriendlyReward.csv": "b6588b4b708f209b20ae97514ea1afe4",
        "CR_FriendlyReward_Upgrade.csv": "dcb887e3c6d98dd70a534bc10e10d8d9",
        "CR_FriendlyReward_Upgrade_Item.csv": "9ffeea8b22ee1fc3dac7390d6c4b9f72",
        "CR_LevelupReward.csv": "ce7672f0a29af13a9a60e8a91f6b7a8b",
        "CR_LevelupReward_Cmu_Table.csv": "7b4d352f824e1f75331c55b91e33d015",
        "CR_LevelupReward_Degree_Table.csv": "7b4d352f824e1f75331c55b91e33d015",
        "CR_LevelupReward_Item_Table.csv": "7b4d352f824e1f75331c55b91e33d015",
        "CR_LevelupReward_Pose_Table.csv": "7b4d352f824e1f75331c55b91e33d015",
        "CR_Request.csv": "c614cb518695996d5c6b1708cf88941e",
        "CR_Request_Challenge_Condition.csv": "fba3aa25dfe5f681d711ba45968ba457",
        "CR_Request_Condition.csv": "52b1163449162a45d032cfb55903dd89",
        "CR_Request_Drop.csv": "1fecaf9a2eb2d4dbabecf0c0fb9998cc",
        "CR_Request_Reward_Item.csv": "191f0a0084ad844bfba5cf36cbb41c0c",
        "CR_Request_Reward_Table.csv": "df5a0d9adaca165be6ea4304e101bd2a",
        "CR_Request_Trend.csv": "6f7a504277690ee9fba6e4b38b29ee00",
        "CR_Request_Trend_Parameter.csv": "6b96e7000d3e5835e6e5779326d4141e",
        "Donketsu_Data.csv": "ada64b7a70b3cf6b520a64e5ee5e4bae",
        "EpisodeList.csv": "e86a50f5eb2414088505a189fc4245bb",
        "EquipItemOffset.csv": "d45550bf3a921bbe12cdaf160e91a6a3",
        "Equipment_Parameter.csv": "e8eefa81ead06204abe9db4078e2f587",
        "Gacha.csv": "501b34a5a5fac20e2cb23d7f16547386",
        "GachaButtonPop.csv": "167aa8c3518c7d093e4f4b93509aebb3",
        "GachaExternalCharacters.csv": "4a5325a482fc4d7dafed1a59a2b70faf",
        "GachaPopAndTexture.csv": "27f3fe2eee12a540f68626cd8dff4d78",
        "GachaRewardItem.csv": "616d23aea3a1d9abb75a630f92e08562",
        "GachaRewardTable.csv": "cbcf33e8113d26af2e5c40135413908b",
        "GachaStepup.csv": "bf161387e87d0229d3a55be611ae9cc5",
        "GameParameters.csv": "bc55c595529e8108b290012c17a513aa",
        "giftbox_message.csv": "d651afdc474ce9632298e4b1d7ac5c58",
        "girl_accessory_cost_table.csv": "b74a19404a5cd0f1a42c662de3f9e8d3",
        "Girl_Affection_Level.csv": "1db05e468dd2cbc8a551ecc67a693ba7",
        "Girl_Affectionup_Cmu_Table.csv": "d22c283f628253b5e8e0507b3abc6d61",
        "Girl_Affectionup_Deg_Table.csv": "2f4f7555b11300f6245ff48e511f1dd3",
        "Girl_Affectionup_Extra_Reward.csv": "a4fe3e5be73282f5c34be175a2b925c8",
        "Girl_Affectionup_Item_Table.csv": "751d85a880bc4b8352b79efbbf4c1a6c",
        "Girl_Affectionup_Pose_Table.csv": "1eb7b3965c053dbc3997133e2df2470f",
        "Girl_Affectionup_Reward.csv": "44e4752f6e1ac824265d92509fbd9faf",
        "Girl_Affectionup_Voice_Table.csv": "d05adfd58139f70ee3e58408d8ce3594",
        "girl_level_table.csv": "b09b2ad43403b6ab521cb9adae1162d0",
        "Girl_Levelup_Cmu_Table.csv": "f80bcd39f45ae9b28210e9ea78fd8583",
        "Girl_Levelup_Degree_Table.csv": "2ef6a5b23eba985b7b64dd444f6bd0fb",
        "Girl_Levelup_Item_Table.csv": "aa9a26eb19d46d427ecab788a88d13c4",
        "Girl_Levelup_Pose_Table.csv": "1eb7b3965c053dbc3997133e2df2470f",
        "Girl_Levelup_Reward.csv": "1ab3c813fc4764d746de1df8f93735e6",
        "girl_master.csv": "4e6aa94b46ab7522b278bf25eeb0068c",
        "girl_status_table.csv": "77766dee8017774185d8701fa5a0f0a4",
        "GravurePanelData.csv": "e44e0172bc190a09298372fc2b6400a3",
        "GravurePanelRelease.csv": "930f319ee646e386b6b193d7d19bbcaf",
        "Honor.csv": "7d18a1572ad7ed931f94174b85c71719",
        "Honor_Group.csv": "aaa6c207ff250da081ac15637266e604",
        "Item_Addition_Accessary_Setting.csv": "b57bba24fa67786e39be9fcea0f71de3",
        "Item_Addition_Accessary_Table.csv": "5f076986b995eba04d662e67209a5760",
        "Item_Decompose_Add.csv": "8c95dc9ad5c2134b81f7a105ec04bf6a",
        "Item_Decompose_Add_Group.csv": "1f3863c258b13f7170a98834fff7590f",
        "Item_Decompose_Table.csv": "6d9682d0ac95623f180ea298b786c76a",
        "Item_Ex_Cost_Table.csv": "c05472b44e9e824ea2c5349e8e301344",
        "Item_Level_Change.csv": "b62423c0e80326a8395f98df1a1ca2bd",
        "Item_Level_Material_Table.csv": "0a4fc3b38ce93c948d89a77cb14bf3f6",
        "Item_Level_Table.csv": "17b5d94375e26d7783293dac6033aaab",
        "Item_Level_Unlock_Table.csv": "855f42d5baea35bd619d2e815e64e48e",
        "Item_Photospot_Table.csv": "b3aa98ea8266efac955fe5b4e710d024",
        "Item_PoseGrowth_table.csv": "9eba20c94470dc5fff2b5c262fc8f5eb",
        "Item_SkillGrowth_Group.csv": "5f22fb5df4e9358e4140be969c774130",
        "Item_SkillGrowth_Table.csv": "8d329aa0bb1ccae1c643ba5d3412a062",
        "Item_Status_Table.csv": "0887623c2ccdc37daf416ef97156c7bc",
        "Item_Upgrade_Cost_Table.csv": "7dfd346194a520265673cf576a854fdd",
        "Item_Upgrade_Exp_Table.csv": "c9b4b262acae64dbeef0b39c7ea5f5b0",
        "Item_Upgrade_Table.csv": "8b254378b54b3664be8b08457a66bdbe",
        "KTAppExchange.csv": "2b6988721938100bd92c46ad19d26886",
        "LessonCampaign.csv": "6b9d548f15440842a18b399800e42fbc",
        "LessonClearRank.csv": "e00c86b30947ddd1df9fc968a5e7bb24",
        "LessonCoord.csv": "dbdb874e17954bba59fb1bde599ac6c1",
        "LessonDrop.csv": "4ac6ebfec177236ad281c834c6894772",
        "LessonInfo.csv": "04d08c0bc9f92e55d5aac0754f1c50e7",
        "LessonPotential.csv": "73209bf9478859cceeb1db4f762335f1",
        "LessonRewardItem.csv": "32e112e75d5d9ec7f02b44358984f3ff",
        "LessonRewardTable.csv": "5f5e325570ae531c5f35cb03446a9a17",
        "LessonUnlock.csv": "15fd7d94ffdb24adf1343aa91c13b348",
        "LoginBonus.csv": "44c4894495687d43be4941789877d1e2",
        "LoginBonusDetail.csv": "755868ced3a41bc2245df031374b35a8",
        "LoginMessageMapping.csv": "3831efc800b4fc5033c403165f0cecc5",
        "LoginMonthlyTicketLink.csv": "2be19638fd4d93f051f0dd3e860cf582",
        "MissionClearCondition.csv": "1edda6b2930e39532454b7258f9d326f",
        "MissionData.csv": "da5d4c6d749a936d9e955ff9f35a73ec",
        "MissionOpenCondition.csv": "4dcaea6b98c3e5b4e0ae3ee2e0c20892",
        "MissionPanelData.csv": "2bc5a532b2ebe31efe2e79e5f3ce807e",
        "MissionReward.csv": "05ca7daa0673aa595af4d682f89fd847",
        "MissionSpecialCondition.csv": "a8ca6f6c5289d86b78708b6bb4238788",
        "NG_word_DMM.csv": "b702affcb354f84b9ea847763877aa0e",
        "NG_word_KT.csv": "3d08b1d1d9f362b183cd938c29890186",
        "NG_word_STEAM.csv": "b638da358f8fe5175945a60e8e429472",
        "OnsenDrop.csv": "b560ab851b2c667a43450130560ecd36",
        "OnsenGaugeItem.csv": "5ff0efb634fb3d231307a9a139abf9fd",
        "OnsenQuality.csv": "781eb1fc3fa76ba509bd6c2426dc3829",
        "OnsenRewardItem.csv": "e44a262fb66c02569cd7c20db7f0c5b1",
        "OnsenRewardTable.csv": "e5b948ac2bdd077ff56609cae0b77da0",
        "owner_level_table.csv": "d4dfe86818c5074f47361200e83f7d6c",
        "owner_rank.csv": "85f268cd6f51b6efd2cf5906485c9462",
        "owner_rank_bonus.csv": "ab2d40350a4e0a505d4d1cc812303345",
        "owner_stamina_table.csv": "573388690da70f47f32879a47cbc2865",
        "OwnerReferralMissionData.csv": "53420952c5ef71c93ff3f4d2539b4571",
        "PosecardPrice.csv": "898dab8524de810cbc6c5b290ff0b259",
        "PosecardShop.csv": "63af989107372fc65bc72cb7438b9af1",
        "PosecardShopItemDetail.csv": "83d6f25e77d53ce46273610417bab412",
        "PosecardShopItemDiscountLink.csv": "28fa8c2903100f4c6f2fe3eaf0b86c39",
        "PosecardShopItemList.csv": "d6799f6ab19a521bcad29a4e8bc52797",
        "PosecardShopPointTypeLink.csv": "9f0b5d6ef10a74438ca3156250de03f0",
        "PosecardShopSaleInfo.csv": "f97b06b5ab3fb6114e4f8d10fadef27a",
        "PresentBonus.csv": "09d1c5dc74cf539f84e5e4cd70742c48",
        "PresentDefiniteEx.csv": "8858817eb8561dc29bdb1593755dc44e",
        "PresentDirectionRate.csv": "9cd0f8b3516515d63799aba7a092b667",
        "PresentDirectionRateEx.csv": "47b6eefb6bd432299a089c42c615cab6",
        "PresentGirlLimitedItem.csv": "f322ed926e81ea5bcb46b975631915db",
        "PresentReturn.csv": "6e8854d4fbea441caf643186132369db",
        "PresentReturnEx.csv": "3879ead45a57f5957b6f897be86ed62b",
        "PresentReturnItem.csv": "27d7ea85d2d6549ad179d0ea57fc2b03",
        "PresentReturnItemEx.csv": "5066ee968993306f5f1a0dbd6b1ae897",
        "Price.csv": "e8ae99661985b937bdd7d639016002ba",
        "PyonPyon_Course.csv": "6434cc373ccad818c81a9fdb324937fe",
        "PyonPyon_Dice.csv": "3f27f4dc704bd953daa129853e92fb96",
        "PyonPyon_RewardItem.csv": "8c73e6fec2771bb925e081e23bbc04bf",
        "PyonPyon_Stage.csv": "d2192f0e10b11302a959311f546e3bda",
        "QuestAbleAutoChallengeCategory.csv": "3ce10634013fdd827ec14bfa969affb9",
        "QuestAbleAutoPlayCategory.csv": "c3a4130acc3aa03d9fdf77e3fa520be4",
        "QuestChallengeFesData.csv": "29fa010966d0a524ff1b47cf8813f30d",
        "QuestClearPrizeData.csv": "8d074d3b83b02ecfa22be8caaeb39904",
        "QuestConditionData.csv": "2252c553c5a6bbb81e9224cff2a3a27b",
        "QuestDailyLimitNumberData.csv": "9d8ff0afc8563a413bde589ad12a45d2",
        "QuestData.csv": "93d83596961d53c1986a8f81caf3785f",
        "QuestEnemyData.csv": "b0327f69b9558b097007607c487b7460",
        "QuestFesData.csv": "5eb18a6fcd7122353051d164248a1859",
        "QuestFirstClearPrizeData.csv": "f7634c08810ecde5f362c93bfa403517",
        "QuestLicenseLevelData.csv": "20446701651606fd5719051232344632",
        "QuestMatchData.csv": "a4207c035580bbcf71ee7f5f4de31a25",
        "QuestMatchingOwnerRankPrize.csv": "f040d36300f154eee6b663b43ded3a16",
        "QuestRankBorderData.csv": "773639550542f16233f4eca33a399d2e",
        "QuestSRankClearPrizeData.csv": "19b6dfe59843f599892b44d89788bb5f",
        "Ranking.csv": "41c2b6fa9e5ecb066193db92b9cdffb8",
        "RankingBeachFlag.csv": "1e456f5b50093f83acc0023ed186d38b",
        "RankingDonketsu.csv": "40e03b4dac95f9b55619ec105e195fa3",
        "RankingFes.csv": "1aefb31fc6e5304fbf4963e852d89702",
        "RankingIDToItemID.csv": "14773d49079d8f0a1f4f4485634ce545",
        "RankingItem.csv": "e850b0b726fbb2d4f65cf7a53884069f",
        "RankingPointReward.csv": "e3ee6b14e429759be6862060db3cbe62",
        "RankingRaidReward.csv": "04dddb89eba6ad7c23d0f61701386553",
        "RankingReward.csv": "283a9d8f0b19451baa6aeb6b5fc02416",
        "RockClimbingLongData.csv": "f649410bc45165f07c5b05eaca9cd023",
        "RockClimbingShortData.csv": "199bfdc635202ae7dde04fe41e8f7917",
        "Roulette_BetIndexData.csv": "c203849401e1469f5df4af5f61d977f5",
        "Roulette_BetTypeToOdds.csv": "13719ddd326338b35502d776825feb1a",
        "SealBase.csv": "cc496a30a9d4ed1a71c2f8df1ac2cfa9",
        "SealExpItem.csv": "fdbae379bb2a2198bb5adea6b4496244",
        "SealSetting.csv": "8ec16966d12678ff90e8af82e355d0f2",
        "SealSkillCorrect.csv": "b32f8c794651b44d3d6c253bc68a51cc",
        "SealUpgrade.csv": "33a01f65f1e24dbce406d2abfa9d4aa0",
        "Shop.csv": "03b8ed6f4b3cbad782814eabc430d139",
        "ShopCategory.csv": "96b7ad26bebe9f6d6e3db181808172a1",
        "ShopItemDetail.csv": "d82da1f321673b168d6751ade780874d",
        "ShopItemDiscountLink.csv": "4407c634c016e538e4b29efe6c0a7478",
        "ShopItemList.csv": "53c9199099aed7b597ed328938b98457",
        "ShopPointTypeLink.csv": "c4b4e86cd56e9242b7d206c41e37dd3f",
        "ShopSaleInfo.csv": "8fbd2cbc2886c9b0a04c4dac5e5824a2",
        "skill.csv": "204a8358314e8dde95ad405945b554a3",
        "skill_char.csv": "ce54bd900d54e499d48a1f1a021374c7",
        "skill_efct_growth.csv": "3f8ea0367662f43d0b8c76d6a8ce398e",
        "skill_polishing_exp_item.csv": "5dbcc06dff27cb578a1685592555a2ce",
        "skill_polishing_exp_table.csv": "59a8f50c5008994c20776736e1ad96a3",
        "skill_polishing_pp_growth.csv": "a83c4e5e678074592efee0ecc93c3aa0",
        "skill_rock_climbing_efct_growth.csv": "ef4b0968c7f5e8e0455e8e6d776dafc0",
        "skill_rock_climbing_exp.csv": "ca5afbc6b3ca5d943b974a90fa9e12f8",
        "skill_rock_climbing_pp_growth.csv": "044465b8e17765c9acec03ba1780d495",
        "skill_rock_climbing_trig_growth.csv": "d390b5b0ce4d12cd2ffd7e288371a9d4",
        "skill_trig_growth.csv": "245279b013a2648f1fdae22c87cf4662",
        "subscription.csv": "2d428eba792fcb84b472712ac6289fdb",
        "subscription_details.csv": "912e174bef2350e55a4799a1144eee48",
        "TrendBonus.csv": "f37cbc59f7aaf9a96b3108c3d2fdc6fa",
        "TrendEventFes.csv": "56e3c38ddc206810aa2da904f36f3858",
        "TrendFesList.csv": "66dd8fb5106dea7089e52bd5dcedba63",
        "TrendKizunaIdList.csv": "138d3bdb5b4dd74a16851d8fe84bea75",
        "TrendMainFes.csv": "06259f5ed079c292fac34089ae778a04",
        "TrendPresentIdList.csv": "b8479a65d44dd3f5aa37eef569b5c19b",
        "TrendPresentSupportGroupIdList.csv": "2979bfe88066d263314586c5ff3ad04f",
        "TrendPvpSeasonalBonus.csv": "f9e18926e1b95c79117429bd36d72efa",
        "VenusBoard_KPIPanelType.csv": "b12ae67aa110b1dbb663859fa922a321",
        "VenusBoard_Link.csv": "802052acc22193395dcf362cba33b2cd",
        "VenusBoard_Map.csv": "1110cc829641fcda487fa27966506091",
        "VenusBoard_Panel.csv": "b97d21c620735a388ab80bcd826486cd",
        "VenusBoard_PanelCondition.csv": "7d305e721885b405e2a67a89676dc2fd",
        "VenusBoard_PanelReward.csv": "8a01d509a207c7baeb0437949f230edf",
        "VenusBoard_ReleaseGirls.csv": "6d8d011c9b24024f72491e285147c9c6",
        "version_info.csv": "543d0e9051aadd2eeb1a61d45479a96b",
        "voting.csv": "516b8e79360722200095464f1018fb2e",
        "voting_candidate.csv": "ea9d228af805ac94bbc282b52f0a1a55",
        "YwrkSkillTable.csv": "d8ec72017d0a964b0759ae81c2eebcdb",
        "file_encrypt_key": "9AraWdtpsar4fln2r1TtX0AxiCJcLSqp",
    }
}
CSV_FILE_HEADERS = {
    10: {
        "EpisodeList.csv": [
            None,
            "episode_mid",
            None,
            None,
            "experience_gain",
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        "GravurePanelData.csv": [None, None, None, None, None, "episode_mid"],
    }
}


@functools.cache
def get_csv_dir() -> Path:
    return config.DATA_DIR / "csv"


@functools.cache
def get_json_dir() -> Path:
    return config.DATA_DIR / "json" / "csv"


@functools.cache
def get_schema_dir() -> Path:
    return config.DATA_DIR / "schema" / "csv"


@functools.cache
def get_model_dir() -> Path:
    return config.DATA_DIR / "model" / "csv"


def decrypt_file(key: str, path: Path) -> bytes:
    decrypted_data = utils.decrypt_data(
        AES(key.encode()),
        path.read_bytes(),
        bytes.fromhex(path.name),
    )
    uncompressed_data = gzip.decompress(decrypted_data)
    return uncompressed_data


def game_to_csv():
    shutil.rmtree(get_csv_dir(), True)

    for master_version, csv_file_list in CSV_FILE_LISTS.items():
        file_encrypt_key = csv_file_list.pop("file_encrypt_key")
        md5 = hashlib.md5(file_encrypt_key.encode())
        md5.update(str(master_version).encode())
        key = md5.hexdigest()

        src_path = config.DATA_DIR / "game" / "production" / "csv" / str(master_version)
        dst_path = get_csv_dir() / str(master_version)
        for csv_file, initialization_vector in csv_file_list.items():
            encrypted_path = src_path / initialization_vector
            if encrypted_path.is_file():
                logging.info(f"[ENCRYPTED] {encrypted_path}")

                data = decrypt_file(key, encrypted_path)
                if csv_file in CSV_FILE_HEADERS.get(master_version, {}):
                    fieldnames = CSV_FILE_HEADERS[master_version][csv_file]
                    for index in range(len(fieldnames)):
                        if fieldnames[index] is None:
                            fieldnames[index] = f"column_{index + 1}"

                    string_io = StringIO()
                    dict_writer = DictWriter(
                        string_io, fieldnames, quoting=csv.QUOTE_ALL
                    )
                    dict_writer.writeheader()
                    data = string_io.getvalue().encode() + data

                csv_path = dst_path / csv_file
                logging.warning(f"[CSV] {csv_path}")

                csv_path.parent.mkdir(parents=True, exist_ok=True)
                csv_path.write_bytes(data)
            else:
                logging.error(encrypted_path)


def isint(self: str) -> bool:
    return self[self[0] == "-" :].isdigit()


def csv_to_json(path: Path):
    logging.info(f"[CSV] {path}")

    dst_path = get_json_dir() / path.parent.name / path.stem
    dst_path.mkdir(parents=True, exist_ok=True)
    with path.open() as file:
        dict_reader = DictReader(file, quoting=csv.QUOTE_ALL)

        for index, data in enumerate(dict_reader, 1):
            for key, value in data.items():
                if value == "":
                    data[key] = None
                elif isint(value):
                    data[key] = int(value)

            path_name = f"row_{index}.json"
            json_path = dst_path / path_name

            logging.warning(f"[JSON] {json_path}")
            json_path.write_text(json.dumps(data))


def to_model():
    game_to_csv()

    shutil.rmtree(get_json_dir(), True)
    for master_version, csv_files in CSV_FILE_HEADERS.items():
        base_path = get_csv_dir() / str(master_version)
        for csv_file in csv_files:
            csv_path = base_path / csv_file
            if csv_path.is_file():
                csv_to_json(csv_path)

    shutil.rmtree(get_schema_dir(), True)
    path_paths = set()
    for json_path in (get_json_dir()).rglob("*.json"):
        if json_path.is_file():
            path_paths.add(json_path.parent)
    for path_path in path_paths:
        utils.json_to_schema(path_path, get_json_dir(), get_schema_dir())

    shutil.rmtree(get_model_dir(), True)
    for schema_path in (get_schema_dir()).rglob("*.schema.json"):
        if schema_path.is_file():
            utils.schema_to_model(schema_path, get_schema_dir(), get_model_dir())
