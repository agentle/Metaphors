# from bs4 import BeautifulSoup 
# # or if you're using BeautifulSoup4:
# # from bs4 import BeautifulSoup

# soup = BeautifulSoup(requests.get('http://example.com').text)

# for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
#     tds = row('td')
#     print(tds[0].string, tds[1].string)
#     # will print date and sunrise


import re
text = """ Information for "Computer virus" - Wikipedia
document.documentElement.className = document.documentElement.className.replace( /(^|\s)client-nojs(\s|$)/, "$1client-js$2" );
(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":false,"wgNamespaceNumber":0,"wgPageName":"Computer_virus","wgTitle":"Computer virus","wgCurRevisionId":888658317,"wgRevisionId":0,"wgArticleId":18994196,"wgIsArticle":false,"wgIsRedirect":false,"wgAction":"info","wgUserName":null,"wgUserGroups":["*"],"wgCategories":[],"wgBreakFrames":true,"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgMonthNamesShort":["","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"wgRelevantPageName":"Computer_virus","wgRelevantArticleId":18994196,"wgRequestId":"XKr3yQpAICwAAJiagRAAAACO","wgCSPNonce":false,"wgIsProbablyEditable":true,"wgRelevantPageIsProbablyEditable":true,"wgRestrictionEdit":[],"wgRestrictionMove":["sysop"],"wgFlaggedRevsParams":{"tags":{}},"wgStableRevisionId":888658317,"wgCategoryTreePageCategoryOptions":"{\"mode\":0,\"hideprefix\":20,\"showcount\":true,\"namespaces\":false}","wgWikiEditorEnabledModules":[],"wgBetaFeaturesFeatures":[],"wgMediaViewerOnClick":true,"wgMediaViewerEnabledByDefault":true,"wgPopupsReferencePreviews":false,"wgPopupsShouldSendModuleToUser":true,"wgPopupsConflictsWithNavPopupGadget":false,"wgVisualEditor":{"pageLanguageCode":"en","pageLanguageDir":"ltr","pageVariantFallbacks":"en","usePageImages":true,"usePageDescriptions":true},"wgMFDisplayWikibaseDescriptions":{"search":true,"nearby":true,"watchlist":true,"tagline":false},"wgRelatedArticles":null,"wgRelatedArticlesUseCirrusSearch":true,"wgRelatedArticlesOnlyUseCirrusSearch":false,"wgWMESchemaEditAttemptStepOversample":false,"wgPoweredByHHVM":true,"wgULSCurrentAutonym":"English","wgNoticeProject":"wikipedia","wgCentralNoticeCookiesToDelete":[],"wgCentralNoticeCategoriesUsingLegacy":["Fundraising","fundraising"],"wgPageViewInfo":{"graph":{"version":2,"data":[{"name":"pageviews","values":[{"timestamp":"20190308","views":1750},{"timestamp":"20190309","views":1267},{"timestamp":"20190310","views":1474},{"timestamp":"20190311","views":1837},{"timestamp":"20190312","views":2047},{"timestamp":"20190313","views":1982},{"timestamp":"20190314","views":2147},{"timestamp":"20190315","views":1484},{"timestamp":"20190316","views":1272},{"timestamp":"20190317","views":1522},{"timestamp":"20190318","views":1877},{"timestamp":"20190319","views":1771},{"timestamp":"20190320","views":1850},{"timestamp":"20190321","views":1590},{"timestamp":"20190322","views":1627},{"timestamp":"20190323","views":1147},{"timestamp":"20190324","views":1641},{"timestamp":"20190325","views":1764},{"timestamp":"20190326","views":2090},{"timestamp":"20190327","views":1911},{"timestamp":"20190328","views":1743},{"timestamp":"20190329","views":1625},{"timestamp":"20190330","views":1124},{"timestamp":"20190331","views":1500},{"timestamp":"20190401","views":1677},{"timestamp":"20190402","views":1865},{"timestamp":"20190403","views":1818},{"timestamp":"20190404","views":1578},{"timestamp":"20190405","views":1424},{"timestamp":"20190406","views":1088}],"transform":[{"type":"formula","field":"date","expr":"datetime(parseInt(substring(datum.timestamp,0,4)),parseInt(substring(datum.timestamp,4,6))-1,parseInt(substring(datum.timestamp,6,8)))"}]},{"name":"alldata","source":"pageviews","transform":[{"type":"formula","field":"Page views","expr":"datum.views"},{"type":"fold","fields":["Page views"]}]},{"name":"stats","source":"alldata","transform":[{"type":"aggregate","groupby":["date"],"summarize":[{"field":"value","ops":["sum"]}]}]}],"scales":[{"name":"x","type":"time","range":"width","domain":{"data":"alldata","field":"date"}},{"name":"y","type":"linear","range":"height","nice":true,"domain":{"data":"stats","field":"sum_value"}},{"name":"c","type":"ordinal","range":["#5DA5DA"],"domain":{"data":"alldata","field":"key"}}],"axes":[{"type":"x","scale":"x","ticks":5},{"type":"y","scale":"y"}],"marks":[{"type":"group","from":{"data":"alldata","transform":[{"type":"stack","groupby":["date"],"sortby":["key"],"field":"value"},{"type":"facet","groupby":["key"]}]},"marks":[{"type":"area","properties":{"enter":{"interpolate":{"value":"monotone"},"x":{"scale":"x","field":"date"},"y":{"scale":"y","field":"layout_start"},"y2":{"scale":"y","field":"layout_end"},"fill":{"scale":"c","field":"key"},"fillOpacity":{"value":1}}}}]}]},"start":"8 March 2019","end":"6 April 2019"},"wgScoreNoteLanguages":{"arabic":"العربية","catalan":"català","deutsch":"Deutsch","english":"English","espanol":"español","italiano":"italiano","nederlands":"Nederlands","norsk":"norsk","portugues":"português","suomi":"suomi","svenska":"svenska","vlaams":"West-Vlams"},"wgScoreDefaultNoteLanguage":"nederlands","wgCentralAuthMobileDomain":false,"wgCodeMirrorEnabled":true,"wgVisualEditorToolbarScrollOffset":0,"wgVisualEditorUnsupportedEditParams":["undo","undoafter","veswitched"],"wgEditSubmitButtonLabelPublish":true,"oresWikiId":"enwiki","oresBaseUrl":"http://ores.discovery.wmnet:8081/","oresApiVersion":3});mw.loader.state({"ext.gadget.charinsert-styles":"ready","ext.globalCssJs.user.styles":"ready","ext.globalCssJs.site.styles":"ready","site.styles":"ready","noscript":"ready","user.styles":"ready","ext.globalCssJs.user":"ready","ext.globalCssJs.site":"ready","user":"ready","user.options":"ready","user.tokens":"loading","mediawiki.legacy.shared":"ready","mediawiki.legacy.commonPrint":"ready","ext.visualEditor.desktopArticleTarget.noscript":"ready","ext.uls.interlanguage":"ready","ext.wikimediaBadges":"ready","ext.3d.styles":"ready","ext.flaggedRevs.basic":"ready","mediawiki.skinning.interface":"ready","skins.vector.styles":"ready"});mw.loader.implement("user.tokens@0tffind",function($,jQuery,require,module){/*@nomin*/mw.user.tokens.set({"editToken":"+\\","patrolToken":"+\\","watchToken":"+\\","csrfToken":"+\\"});
});RLPAGEMODULES=["ext.pageviewinfo","site","mediawiki.page.startup","mediawiki.page.ready","mediawiki.searchSuggest","ext.gadget.teahouse","ext.gadget.ReferenceTooltips","ext.gadget.watchlist-notice","ext.gadget.DRN-wizard","ext.gadget.charinsert","ext.gadget.refToolbar","ext.gadget.extra-toolbar-buttons","ext.gadget.switcher","ext.centralauth.centralautologin","ext.popups","ext.visualEditor.desktopArticleTarget.init","ext.visualEditor.targetLoader","ext.eventLogging","ext.wikimediaEvents","ext.navigationTiming","ext.uls.eventlogger","ext.uls.init","ext.uls.compactlinks","ext.uls.interface","ext.quicksurveys.init","ext.centralNotice.geoIP","ext.centralNotice.startUp","ext.flaggedRevs.advanced","skins.vector.js"];mw.loader.load(RLPAGEMODULES);});































Information for "Computer virus"



Jump to navigation
Jump to search
Help:Page information.mw-hiddenCategoriesExplanation { display: none; }
.mw-templatesUsedExplanation { display: none; }
Basic information

Display titleComputer virus
Default sort keyComputer Virus
Page length (in bytes)81,380
Page ID18994196
Page content languageen - English
Page content modelwikitext
Indexing by robotsAllowed
Number of page watchers479
Number of page watchers who visited recent edits36
Number of redirects to this page37
Counted as a content pageYes
Wikidata item IDQ485
Central descriptionmalicious software program
Page views in the past 30 days49,492

Page protection

EditAllow all users (no expiry set)
MoveRequire administrator access (no expiry set)

View the protection log for this page.
Edit history

Page creatorGreg Lindahl (talk | contribs)
Date of page creation04:17, 29 September 2001
Latest editorBruce1ee (talk | contribs)
Date of latest edit15:49, 20 March 2019
Total number of edits7,109
Recent number of edits (within past 30 days)2
Recent number of distinct authors2

Page properties

Hidden categories (17)This page is a member of 17 hidden categories (help) :

Category:All articles containing potentially dated statements
Category:All articles with unsourced statements
Category:Articles containing potentially dated statements from 2005
Category:Articles with Curlie links
Category:Articles with unsourced statements from January 2019
Category:Articles with unsourced statements from May 2016
Category:CS1: long volume value
Category:CS1 Danish-language sources (da)
Category:CS1 maint: Unfit url
Category:Commons category link is on Wikidata
Category:Webarchive template wayback links
Category:Wikipedia articles with BNF identifiers
Category:Wikipedia articles with GND identifiers
Category:Wikipedia articles with LCCN identifiers
Category:Wikipedia articles with NDL identifiers
Category:Wikipedia indefinitely move-protected pages
Category:Wikipedia pending changes protected pages

Transcluded templates (104)Pages transcluded onto the current version of this page (help) :

Template:As of (view source) (template protected)Template:Authority control (view source) (template protected)Template:Catalog lookup link (view source) (template protected)Template:Category handler (view source) (protected)Template:Citation (view source) (protected)Template:Citation needed (view source) (protected)Template:Cite AV media (view source) (template protected)Template:Cite book (view source) (protected)Template:Cite journal (view source) (protected)Template:Cite magazine (view source) (protected)Template:Cite news (view source) (protected)Template:Cite press release (view source) (protected)Template:Cite video (view source) (protected)Template:Cite web (view source) (protected)Template:Cn (view source) (template protected)Template:Column-width (view source) (template protected)Template:Commons (view source) (template protected)Template:Commons category (view source) (template protected)Template:Curlie (view source) (template protected)Template:DMCA (view source) (template protected)Template:Dated maintenance category (view source) (template protected)Template:Delink (view source) (template protected)Template:Distinguish (view source) (template protected)Template:Div col (view source) (template protected)Template:Div col end (view source) (template protected)Template:Dmoz (view source) (template protected)Template:EditAtWikidata (view source) (template protected)Template:Error-small (view source) (template protected)Template:FULLROOTPAGENAME (view source) (template protected)Template:Fix (view source) (protected)Template:Fix/category (view source) (template protected)Template:ISBN (view source) (template protected)Template:Main other (view source) (protected)Template:Malware (edit) Template:Navbox (view source) (template protected)Template:Ns has subpages (view source) (template protected)Template:Portal (view source) (template protected)Template:Pp-move (view source) (template protected)Template:Pp-move-indef (view source) (template protected)Template:Pp-pc (view source) (template protected)Template:Pp-pc1 (view source) (template protected)Template:Refbegin (view source) (template protected)Template:Refbegin/styles.css (view source) (template protected)Template:Refend (view source) (template protected)Template:Reflist (view source) (protected)Template:Replace (view source) (template protected)Template:See also (view source) (template protected)Template:Side box (view source) (template protected)Template:Sister project (view source) (template protected)Template:Small (view source) (template protected)This list may be incomplete.
Wikidata entities used in this pageInternational Standard Serial NumberSitelinkdigital object identifierSitelinkcomputer virusSitelinkSome statementsOther (Statements)TitleCategory:Computer virusesSitelink

External tools
Revision history search
Revision history statistics
Edits by user
Page view statistics
WikiChecker
Retrieved from "https://en.wikipedia.org/wiki/Computer_virus"





Navigation menu


Personal tools

Not logged inTalkContributionsCreate accountLog in 



Namespaces

ArticleTalk 




Variants







Views

ReadEditView history 



More





Search



 







Navigation


Main pageContentsFeatured contentCurrent eventsRandom articleDonate to WikipediaWikipedia store 



Interaction


HelpAbout WikipediaCommunity portalRecent changesContact page 



Tools


What links hereRelated changesUpload fileSpecial pagesPage informationWikidata item 



Languages









Privacy policy
About Wikipedia
Disclaimers
Contact Wikipedia
Developers
Cookie statement
Mobile view



 

 



(window.RLQ=window.RLQ||[]).push(function(){mw.config.set({"wgBackendResponseTime":271,"wgHostname":"mw1323"});});

"""
match = re.search("Date", """)
Date of page creation04:17, 29 September 2001""")
print(match)
