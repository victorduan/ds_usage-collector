delimiter $$

CREATE TABLE `usage_reporting` (
  `intID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `start` int(11) unsigned NOT NULL,
  `end` int(11) unsigned NOT NULL,
  `stream_type` varchar(45) NOT NULL,
  `stream_hash` varchar(45) NOT NULL,
  `seconds` int(11) NOT NULL DEFAULT '0',
  `interaction` int(10) unsigned DEFAULT '0',
  `twitter` int(10) unsigned DEFAULT '0',
  `facebook` int(10) unsigned DEFAULT '0',
  `youtube` int(10) unsigned DEFAULT '0',
  `gender` int(10) unsigned DEFAULT '0',
  `language` int(10) unsigned DEFAULT '0',
  `links` int(10) unsigned DEFAULT '0',
  `trends` int(10) unsigned DEFAULT '0',
  `2ch` int(10) unsigned DEFAULT '0',
  `amazon` int(10) unsigned DEFAULT '0',
  `bitly_trial` int(10) unsigned DEFAULT '0',
  `blog` int(10) unsigned DEFAULT '0',
  `board` int(10) unsigned DEFAULT '0',
  `dailymotion` int(10) unsigned DEFAULT '0',
  `demographics` int(10) unsigned DEFAULT '0',
  `demographics_trial` int(10) unsigned DEFAULT '0',
  `digg` int(10) unsigned DEFAULT '0',
  `flickr` int(10) unsigned DEFAULT '0',
  `klout.profile` int(10) unsigned DEFAULT '0',
  `klout.score` int(10) unsigned DEFAULT '0',
  `klout.topics` int(10) unsigned DEFAULT '0',
  `reddit` int(10) unsigned DEFAULT '0',
  `myspace` int(10) unsigned DEFAULT '0',
  `salience.entities` int(10) unsigned DEFAULT '0',
  `salience.sentiment` int(10) unsigned DEFAULT '0',
  `salience.topics` int(10) unsigned DEFAULT '0',
  `sentiment.topics` int(10) unsigned DEFAULT '0',
  `topix` int(10) unsigned DEFAULT '0',
  `video` int(10) unsigned DEFAULT '0',
  `wordpress.blog` int(10) unsigned DEFAULT '0',
  `wordpress.comment` int(10) unsigned DEFAULT '0',
  `wikipedia` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`intID`),
  KEY `username` (`username`),
  KEY `stream_type` (`stream_type`)
) ENGINE=InnoDB AUTO_INCREMENT=11719 DEFAULT CHARSET=latin1$$

