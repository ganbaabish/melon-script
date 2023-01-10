import time
import tweepy
import requests
import datetime

target_id = 74367327

date_format = "%Y-%m-%d %H:%M:%S"

#************************** Zayabaatar api keys **********************************#

"""configuration"""
url = 'https://trends.melon.mn/melon/public'
zayabaatar_tokens = {}
ganbat_tokens = {}
elevated_tokens = {}

zayabaatar_tokens['consumer_key'] = '5p1Nb1r3TI53H8xv7uONSnSIy'
zayabaatar_tokens['consumer_secret'] = 'FEQBTep7yDtW3fYjtqCoXu5Ip2E34VbAjSdNZudXsguFqMYpWH'
zayabaatar_tokens['access_token'] = '74367327-EW9lHQAi3ERZ59uTWGNI4d86AG4csgnkZWSxN3uf7'
zayabaatar_tokens['access_token_secret'] = '1cvS4L2RrJorjELfOFt0NprWV8mADAicUfrvu4er5bh2g'
zayabaatar_tokens['bearer_token'] = 'AAAAAAAAAAAAAAAAAAAAAJF7ZgEAAAAAI4Ya2j5nccICsgokbzSmHQRdvjY%3DKQCW3rfSCXnekxjfSMRwA9tEPENS4zYZSQ0FlkgC5sVdKpOOXS'

# ************************* Ganbat api *******************************

ganbat_tokens['consumer_key'] = 'lrry5mdTzXcg6LaA9VwS7El3S'
ganbat_tokens['consumer_secret'] = 'U6yo6XRXD8RV9fHKioikTZc4BZcczndCtGOlu6D4XG26EYtpi6'
ganbat_tokens['access_token'] = '1364857689751183360-KvzFVw4UHgDaR2sdqU5ZTJ67yC9TdC'
ganbat_tokens['access_token_secret'] = 'lhgpCjPNR6s1hprXZqjw4OFJVYBFb3vOqi2s0z4s2ktgw'
ganbat_tokens['bearer_token'] = 'AAAAAAAAAAAAAAAAAAAAAOXFYgEAAAAAwq9BzuttRGA9fzl3XbKxZQj296o%3DldHi3CyFQRES3jgXBLu8tlMEPwmW6FbKhChPsSNu1s4bTKV1ei'

# ************************ Ganbat elevated keys **************************

elevated_tokens['access_token'] = [
    '1501954775801233410-iifFMD6WrJTJO6FGKJ6uQRrj3VMvlj',
    '1501954775801233410-evRziSCqZIRXORnJqRZNcNICxOX3YE',
    '1501954775801233410-6OgBgoXd4Xu0dh8sz2c93Ky6xK8uZ3'
]
elevated_tokens['access_token_secret'] = [
    'X5RTKA99PkYkATDntLCiNkEzrSx94BgG50Z1sI8Ll2IMB',
    'wgcMRRcztnPVmNxtZORMZMo47ezRQFYU8Y3124gPADEmD',
    'focr4fT5c7OcPo2pLGMgPNd6EdjpXvG6thOxqVF7gBSf1'
]
elevated_tokens['consumer_key'] = [
    'b2YCU3sfSdJZhnMjFacbTbmPi',
    '5oK6IXp16XEI13Otq22sKdCz3',
    '0GnBuGxta6E3J2g9S3NB6BbBW'
]
elevated_tokens['consumer_secret'] = [
    'be5uIOkbBaLazNnnG26dOFsamHA6DdNtBvkCiwXXMElXcjKA84',
    'tMROwPFQcd8uYlvpQd5tC2dMKnpJ3IsWCpimy63McfkuoXj3A5',
    'DIfKfTHjgow1U7zQ4ADdRPxp8a7M3OYgZvp5gJeBwZAVHjIVRx'
]
elevated_tokens['bearer_token'] = [
    'AAAAAAAAAAAAAAAAAAAAAE1VaAEAAAAA8fLcaL%2FhbHkUc%2B1voFkmcKqe0fs%3DXRBDshv7Xd3i8FRTbHxS11LLSEkf0gEdiwoUFi9ojRcyvnjDKb',
    'AAAAAAAAAAAAAAAAAAAAAF82aQEAAAAAVmqbpdhtxdGTAVLNKb7wI4QzaHk%3DPofB3kDUvWOIIcyZZ2Jdn86yqztb8tKlmyCbXY5qlr303Tbtpj',
    'AAAAAAAAAAAAAAAAAAAAAHE2aQEAAAAAPccsmw%2FYMJ%2FsnB%2Fr%2FaFIWiFfc8w%3DyNc8N2F5NB4NBBXSO8RfKQW7jw0t1REgNxNt4oZBEajLgSBwBB'
]

class twitter_crawler:
    def __init__(self) -> None:
        self.consumer_key = ganbat_tokens['consumer_key']
        self.consumer_secret = ganbat_tokens['consumer_secret']
        self.access_token = ganbat_tokens['access_token']
        self.access_token_secret = ganbat_tokens['access_token_secret']
        self.bearer_token = ganbat_tokens['bearer_token']
        self._key_name = 'ganbat'
        self.index = 0
        self.elevated_tokens_access_token = elevated_tokens['access_token'][self.index]
        self.elevated_tokens_access_token_secret = elevated_tokens['access_token_secret'][self.index]
        self.elevated_tokens_consumer_key = elevated_tokens['consumer_key'][self.index]
        self.elevated_tokens_consumer_secret = elevated_tokens['consumer_secret'][self.index]
        self.elevated_tokens_bearer_token = elevated_tokens['bearer_token'][self.index]

    def __change_elevated(self):
        if self.index == 2:
            self.index = 0
        else:
            self.index+=1
        self.elevated_tokens_access_token = elevated_tokens['access_token'][self.index]
        self.elevated_tokens_access_token_secret = elevated_tokens['access_token_secret'][self.index]
        self.elevated_tokens_consumer_key = elevated_tokens['consumer_key'][self.index]
        self.elevated_tokens_consumer_secret = elevated_tokens['consumer_secret'][self.index]
        self.elevated_tokens_bearer_token = elevated_tokens['bearer_token'][self.index]

    def __change_keys(self):
        if self._key_name == 'ganbat':
            self.consumer_key = zayabaatar_tokens['consumer_key']
            self.consumer_secret = zayabaatar_tokens['consumer_secret']
            self.access_token = zayabaatar_tokens['access_token']
            self.access_token_secret = zayabaatar_tokens['access_token_secret']
            self.bearer_token = zayabaatar_tokens['bearer_token']
            self._key_name = 'zayabaatar'
        else:
            self.consumer_key = ganbat_tokens['consumer_key']
            self.consumer_secret = ganbat_tokens['consumer_secret']
            self.access_token = ganbat_tokens['access_token']
            self.access_token_secret = ganbat_tokens['access_token_secret']
            self.bearer_token = ganbat_tokens['bearer_token']
            self._key_name = 'ganbat'


    def __start_time(self) -> str:
        return (datetime.datetime.now() - datetime.timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")

    def __take_score(self, elemtent):
        return elemtent['score']

    def __take_key(self, element):
        return element['count']

    def __run(self):
        client = tweepy.Client(
                                consumer_key = self.consumer_key,
                                consumer_secret = self.consumer_secret,
                                access_token = self.access_token,
                                access_token_secret = self.access_token_secret,
                                bearer_token = self.bearer_token,
                                )
        print("Now:", datetime.datetime.now())



        tweeted_user_count = user_count_without_tweets = 0
        all_user = []
        all_tweets = []
        print("Downloading tweets")

            # *******************************getting users more than 100 ********************************
        for users in tweepy.Paginator(client.get_users_following, target_id, user_fields=['public_metrics'], max_results=1000, limit=10):

            #********************************loop for each more than 100 users **********************************************
            for user in users.data:
                user_data = {"user_name": user.username, 
                            "name": user.name,
                            "user_id": user.id,
                            "count_followers": user.public_metrics['followers_count']}
                all_user.append(user_data)
                #***************getting 5 tweets for each users*****************
                tweets = client.get_users_tweets(
                                    id = user.id,
                                    tweet_fields = ['public_metrics', 'created_at'],
                                    max_results = 5,
                                    exclude = ['replies', 'retweets'], 
                                    start_time = self.__start_time()                           #tweet's created date must be within 24 hours
                                    )
                #************************* trying to access to user tweets, if there is no tweet, exception will be raised ******************************
                try:
                    for tweet in tweets.data:
                        tweet_data = {'user_id': user_data['user_id'],
                                    'tweet_id': tweet.id,
                                    'tweet_text': tweet.text,
                                    'count_like': tweet.public_metrics['like_count'],
                                    'count_reply': tweet.public_metrics['reply_count'],
                                    'count_retweet': tweet.public_metrics['retweet_count'],
                                    'created_at': (datetime.datetime.strftime(tweet.created_at, date_format))}
                        all_tweets.append(tweet_data)
                    tweeted_user_count += 1
                except:
                    user_count_without_tweets += 1
            #******** inserting tweet and user data using api, json format ***************************
        user_request = requests.post(url+"/api/users", json=all_user)
        request_for_tweets = requests.post(url+"/api/tweets", json=all_tweets)

        print("User result:")
        print(user_request.json())
        print("Tweet result:")
        print("Exception:", request_for_tweets.json()[0]["exception"])
        print(request_for_tweets.json()[1]["inserted"], "numbers of tweets downloaded")
        print(request_for_tweets.json()[2]["updated"], "numbers of tweets updated")
        print(tweeted_user_count, "numbers of users where tweeted in past 24 hours")
        print(user_count_without_tweets, "numbers of users that you are currently following haven't tweeted in past 24 hours...!")

        #************ getting all tweets that collected in last 24 hours using own website api ************
        data = {"created_at": self.__start_time()}
        req = requests.post(url+"/api/tweets_for_words", data=data)


        tweets = []
        words = []
        data = []

        # formatting tweet text
        for tweet in req.json():
            for text in tweet['tweet_text'].split(" " or "..."):
                temp = str(text).replace('\,', '').\
                    replace('\"', '').\
                        replace(',', '').\
                            replace('.', '').\
                                replace('-', '').\
                                    replace('(', '').\
                                        replace(')', '')
                if len(temp) > 1:
                    tweets.append(temp.lower())
        print("All word count", len(tweets), datetime.datetime.now())
        restricted_words = (requests.get(url+"/api/restricted_words")).json()

        def check_word(word):
            for i in restricted_words:
                if i['word'] == word:
                    return False
            return True

        for word in tweets:
            if word not in words and check_word(word):
                data.append({'word': word, 'count': tweets.count(word)})
                words.append(word)
        arr = []
        print('Unique word count:', len(words), datetime.datetime.now())

        # clearing words
        for line in data:
            temp = str(line['word'])
            check = True
            if temp in words:
                if 'ын' in temp:
                    temp = temp.replace('ын', '')
                    check = False
                elif 'ийн' == temp[len(temp)-4:len(temp)-1]:
                    temp = temp.replace('ийн', '')
                    check = False
                elif 'ны' in temp:
                    temp = temp.replace('ны', '')
                    check = False
                elif 'ний' == temp[len(temp)-4:len(temp)-1]:
                    temp = temp.replace('ийн', '')
                    check = False
                elif 'ыг' in temp:
                    temp = temp.replace('ыг', '')
                    check = False
                elif 'ийг' in temp:
                    temp = temp.replace('йг', '')
                    check = False
                elif 'тай' in temp:
                    temp = temp.replace('тай', '')
                    check = False
                elif 'тэй' in temp:
                    temp = temp.replace('тэй', '')
                    check = False
                elif 'той' in temp:
                    temp = temp.replace('той', '')
                    check = False
                elif temp[len(temp)-1] == 'д' and len(temp) > 2:
                    temp = temp.replace('д', '')
                    check = False
                elif temp[len(temp)-1] == 'т' and len(temp) > 2:
                    temp = temp.replace('т', '')
                    check = False
                if check:
                    if temp in words:
                        count = 0
                        try:
                            count = int(line['count'])
                            arr.remove({'word': temp, 'count': tweets.count(line['word'])})
                            arr.append({'word': temp, 'count': (int(line['count'])+count+tweets.count(line['word']))})
                        except:
                            arr.append({'word': temp, 'count': (int(line['count'])+count+tweets.count(line['word']))})
                            words.remove(temp)
                    else:
                        arr.append({'word': temp, 'count': tweets.count(temp)})
                else:
                    arr.append(line)
        data = sorted(arr, key=self.__take_key, reverse=True)
        all_trending_tweets = []
        print("Downloading trending tweets...!")

        # downloading trending tweets by keyword
        for i in range(10):
            # print(data[i])
            word = data[i]['word']
            num_of_tweets = 0
            try:
                client = tweepy.Client(
                            bearer_token=self.elevated_tokens_access_token,
                            consumer_key=self.elevated_tokens_access_token_secret,
                            consumer_secret=self.elevated_tokens_consumer_key,
                            access_token=self.elevated_tokens_consumer_secret,
                            access_token_secret=self.elevated_tokens_bearer_token,
                            )
                num_of_tweets = client.get_recent_tweets_count(query=word).meta["total_tweet_count"]
                tweets = client.search_recent_tweets(query=word, max_results=50, tweet_fields=['public_metrics', 'created_at'])
            except tweepy.TooManyRequests:
                try:
                    self.__change_elevated()
                    client = tweepy.Client(
                                bearer_token=self.elevated_tokens_access_token,
                                consumer_key=self.elevated_tokens_access_token_secret,
                                consumer_secret=self.elevated_tokens_consumer_key,
                                access_token=self.elevated_tokens_consumer_secret,
                                access_token_secret=self.elevated_tokens_bearer_token,
                            )
                    num_of_tweets = client.get_recent_tweets_count(query=word).meta["total_tweet_count"]
                    tweets = client.search_recent_tweets(
                                query=word, 
                                max_results=50, 
                                tweet_fields=['public_metrics', 'created_at']
                            )
                except tweepy.BadRequest:
                    continue
            except tweepy.BadRequest:
                continue
            finally:
                for tweet in tweets.data:
                    trending_tweets_data = {'key_word': data[i]['word'], 
                                            'tweet_id': tweet.id, 
                                            'tweet_text': tweet.text, 
                                            'count_like': tweet.public_metrics['like_count'], 
                                            'count_reply': tweet.public_metrics['reply_count'], 
                                            'count_retweet': tweet.public_metrics['retweet_count'], 
                                            'created_at': (datetime.datetime.strftime(tweet.created_at, 
                                                                                            "%Y-%m-%d %H:%M:%S")), 
                                            'added_at': (datetime.datetime.strftime(datetime.datetime.now(), 
                                                                                            "%Y-%m-%d %H:%M:%S"))}
                    all_trending_tweets.append(trending_tweets_data)
                trending_word_data = {'word': data[i]['word'], 
                                    'count': data[i]['count'],
                                    'number_of_tweets': num_of_tweets,
                                    'created_at': datetime.datetime.now()}
                requests.post(url+"/api/trending_words", data=trending_word_data)

        requests.post(url+"/api/trending_tweets", json=all_trending_tweets)

        user_rank = requests.get(url+"/api/get_user_rank")

        # inserting user rank by follower count
        for line in user_rank.json():
            user_rank_data = {"user_name": line["user_name"], 
                            "follower_count": line["count_followers"],
                            "created_at": datetime.datetime.now()}
            requests.post(url+"/api/user_rank", data=user_rank_data)

        tweet_rank_data = {"created_at": self.__start_time()}
        tweet_rank = requests.post(url+"/api/get_tweet_rank", data=tweet_rank_data)

        tweets = []
        for tweet in tweet_rank.json():
            if 'RT' not in tweet["tweet_text"]:
                score = tweet["count_like"] + tweet["count_reply"] + tweet["count_retweet"]
                data = {'tweet_id': tweet["tweet_id"],
                        'tweet_text': tweet["tweet_text"],
                        'count_like': tweet["count_like"],
                        'count_reply': tweet["count_reply"], 
                        'count_retweet': tweet["count_retweet"],
                        'score': score,
                        'created_at': tweet["created_at"],
                        "added_at": datetime.datetime.now()}
                tweets.append(data)
        tweets = sorted(tweets, key=self.__take_score, reverse=True)

        # inserting top 10 tweet rank by score of sum of tweet like, retweet, reply
        for i in range(10):
            try:
                requests.post(url+"/api/tweet_rank", data=tweets[i])
            except IndexError:
                pass
        print("Done...!")
        print("Now", datetime.datetime.now())
        print("Sleeping...!")
        time.sleep(1200)

    def start(self):
        while True:
            try:
                self.__run()
            except tweepy.TooManyRequests:
                self.__change_keys()
                continue
            except tweepy.BadRequest:
                continue
            except IndexError:
                continue
            except Exception:
                time.sleep(3600)
                continue
        
tweet_scraper = twitter_crawler()

tweet_scraper.start()
