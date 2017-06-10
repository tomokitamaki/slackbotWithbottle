# slackbotが動くコンテナを作るためのDockerfile
FROM centos:7.3.1611

# ワーキングディレクトリを指定すべて/root/で実行されるようにする。
WORKDIR /root

# gitとiusリポジトリのインストール
RUN yum update -y && yum upgrade && \
yum install -y git https://centos7.iuscommunity.org/ius-release.rpm

# python3.5のインストール
RUN yum install -y python35u python35u-libs python35u-devel python35u-pip

# 必要なシェルスクリプトをローカルからコピーする
COPY Buildslackbot.sh /root/

# slackへの投稿に必要なAPITOKENが記載されたファイルをローカルからコピーする
COPY APITOKEN.py /root/

# slackbotのインストールとセットアップと起動のスクリプト
CMD ["/root/Buildslackbot.sh"]

