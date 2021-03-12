# -*- coding: utf-8 -*-
import settings
import tweepy

# ---------------------------------------------------
# 各種ツイッターのキーをセット
consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET
access_key = settings.ACCESS_KEY
access_secret = settings.ACCESS_SECRET

# tweepyの設定（認証情報を設定）
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
# tweepyの設定（APIインスタンスの作成）
api = tweepy.API(auth, wait_on_rate_limit=True)
# ---------------------------------------------------

# リツイート対象アカウントを指定
users = ["youtubemasterd7", "yako_tera", "mon_youtubeking", "KoolNero", "bazyama", "J1nTube", "afro_three", "naaachanel_", "zirazirakuzira", "yt_map", "nabeno_kitchen", "i_ga_ru", "Mongolianfriend", "jinjin3578", "YouTube_inouet", "Half_Dr", "titikuriikuo", "subtube_yukichi","dunyts", "KoolNero", "yossh1_ch", "taiga_hayami"]
#YoutubeマスターD, ヤコ, もん, 野良ネロ, バズ山, じん, アフロ, なーちゃんねる, YouTubeくじら, 生パスタ, なべ, いがる, Jey, じん(天才), 井上泰介, MIKIO, 乳栗育男, 副業ユキチ, づん, 野良ネコ, よっしー, TAIGA 合計22

sum = 0
for user in users:  # 対象者一人ずつ実行
	results = api.user_timeline(screen_name=user, count=20)  # 過去の20投稿を取得
	for result in results:
		if result.user.followers_count > 10000:  #フォロワーの数で、いいねの基準値を変更する
			like = 80
			if "@" in result.text:
				pass
				#RTや返信は除外する
			else:
				if result.favorite_count > like:  # いいねの基準値を超えた場合実行
					try:
						result.retweet()  # リツイートを実行
						sum += 1  # リツイートの実行数をカウント
						print("ユーザー名"+str(result.user.screen_name))
						print("いいねの数"+str(result.favorite_count))
						print("リツイートの数"+str(result.retweet_count))
					except tweepy.error.TweepError:
						pass  # すでにリツイート済投稿は除外する
				else:
					pass  # いいねが少ないものも除外する
		else:
			like = 50
			if "@" in result.text:
				pass  # RTや返信は除外する
			else:
				if result.favorite_count > like:  # いいねの基準値を超えた場合実行
					try:
						result.retweet()  # リツイートを実行
						sum += 1  # リツイートの実行数をカウント
						print("ユーザー名"+str(result.user.screen_name))
						print("いいねの数"+str(result.favorite_count))
						print("リツイートの数"+str(result.retweet_count))
					except tweepy.error.TweepError:
						pass  # すでにリツイート済投稿は除外する
				else:
					pass #いいねが少ないものも除外する
print("合計リツイート数"+str(sum))
