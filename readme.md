11/13/20 Starting next classes on Python
11/15/20 - trying to get plots to show in Sublime text 3
11/16/20 - Started work on my capstone project
11/18/20 - Improving with dataframes. Refactoring javascript programs into python. 
11/19/20 - Updated trade alerter again (proprietary)
11/20/20 - Continuing work on dataframes. 
11/21/20 - Continuing work on dataframes. 
11/22/20 - Completing cert soon. 
11/23/20 - hanging christmas lights
11/24/20 - Continuing to work on my trading program
11/27/20 - I am getting my trade alerter working today (refactoring JS into python) and journaling about 2020 to understand myself better. 
11/28/20 - setting schedules and completed interview with mentor
11/30/20 - updated trading program.
12/1/20 - made sorting functions more modular. 
12/2/20 -  Manipulating and indexing data frames. 
https://campus.datacamp.com/courses/manipulating-dataframes-with-pandas/extracting-and-transforming-data?ex=1
df[collabel][rowlabel]
columns are attributes of a data frame
.loc uses labels, .iloc uses index positions
Selecting only some columns 
accessing data with brackets from a data frame can return a value, a panda series, or a panda data frame. To return a data frame, use nested brackets. 

Out[2]:

               state   total      Obama     Romney  winner   voters
county                                                             
Adams             PA   41973  35.482334  63.112001  Romney    61156
Allegheny         PA  614671  56.640219  42.185820   Obama   924351
Armstrong         PA   28322  30.696985  67.901278  Romney    42147
Beaver            PA   80015  46.032619  52.637630  Romney   115157
Bedford           PA   21444  22.057452  76.986570  Romney    32189
Berks             PA  163253  48.939376  49.528646  Romney   250356
Blair             PA   47631  32.575424  66.133401  Romney    85328
Bradford          PA   22501  36.847251  61.450602  Romney    40490
Bucks             PA  319407  49.966970  48.801686   Obama   435606
Butler            PA   88924  31.920516  66.816607  Romney   122762
Cambria           PA   57718  40.162514  57.978447  Romney    86988
Cameron           PA    1967  34.417895  64.260295  Romney     3651
Carbon            PA   24232  45.559591  52.451304  Romney    39017
Centre            PA   68801  48.948416  48.977486  Romney   112949
Chester           PA  248295  49.228539  49.650617  Romney   337822
Clarion           PA   15227  31.069810  67.170158  Romney    24120
Clearfield        PA   31894  34.780837  63.657741  Romney    51174
Clinton           PA   12663  43.457317  54.813235  Romney    22969
Columbia          PA   24305  42.888295  55.317836  Romney    39888
Crawford          PA   33089  39.360513  58.922905  Romney    54711
Cumberland        PA  109964  39.997636  58.532793  Romney   158194
Dauphin           PA  122625  52.362080  46.351070   Obama   178924
Delaware          PA  272853  60.400655  38.581214   Obama   397338
Elk               PA   12425  41.400402  57.134809  Romney    20302
Erie              PA  112732  57.779512  40.895221   Obama   176851
Fayette           PA   48196  45.317039  53.624782  Romney    91681
Forest            PA    2308  38.734835  59.835355  Romney     3232
Franklin          PA   62802  30.110506  68.583803  Romney    87406
Fulton            PA    6148  21.096291  77.748861  Romney     9344
Greene            PA   13726  40.536209  58.174268  Romney    22663
...              ...     ...        ...        ...     ...      ...
Lebanon           PA   53771  35.288538  63.249707  Romney    81476
Lehigh            PA  144922  53.152040  45.604532   Obama   226453
Luzerne           PA  123741  51.699922  46.847043   Obama   194137
Lycoming          PA   46214  32.682737  65.975678  Romney    68064
McKean            PA   15014  35.033968  63.234315  Romney    25861
Mercer            PA   48065  48.022470  50.564860  Romney    75238
Mifflin           PA   16311  26.111213  72.913984  Romney    24445
Monroe            PA   59312  56.364648  42.318586   Obama   108879
Montgomery        PA  401787  56.637223  42.286834   Obama   551105
Montour           PA    7787  38.859638  59.535123  Romney    13518
Northampton       PA  125883  51.646370  47.061160   Obama   209414
Northumberland    PA   31512  39.324702  58.758568  Romney    54978
Perry             PA   18240  29.769737  68.591009  Romney    27245
Philadelphia      PA  653598  85.224251  14.051451   Obama  1099197
Pike              PA   23164  43.904334  54.882576  Romney    41840
Potter            PA    7205  26.259542  72.158223  Romney    10913
Schuylkill        PA   57505  42.523259  55.918616  Romney    86316
Snyder            PA   14962  31.225772  67.170164  Romney    21573
Somerset          PA   33875  27.808118  70.656827  Romney    51860
Sullivan          PA    2934  35.037491  63.360600  Romney     4242
Susquehanna       PA   17930  38.432794  59.871723  Romney    26163
Tioga             PA   15943  31.694160  66.480587  Romney    26001
Union             PA   16187  37.455983  60.931612  Romney    23950
Venango           PA   20775  35.951865  62.228640  Romney    32773
Warren            PA   16462  41.112866  57.192322  Romney    29111
Washington        PA   90078  42.744066  56.012567  Romney   142331
Wayne             PA   20966  38.815225  59.768196  Romney    32577
Westmoreland      PA  168709  37.567646  61.306154  Romney   238006
Wyoming           PA   11214  42.910647  55.189941  Romney    17255
York              PA  186394  38.695452  59.860296  Romney   280280

[67 rows x 6 columns]
In [2]:
election['total']['Adams']
Out[2]:
41973
In [3]:
election.total['Adams']
Out[3]:
41973
In [4]:
election.loc['York','total']
Out[4]:
186394
In [5]:
election.iloc[66,1]
Out[5]:
186394

Selecting only some columns
In [6]:
election[['voters','total']]

#Slicing Data Frames

#Filtering Data Frames

#Transforming Data Frames
use df.floordiv(12) or np.floor_divide(12)

df.index = df.index.map(str.lower)

#Fancy indexing

stocks.loc(['AAPL', 'MSFT'], '2016-10-05'), :]


#Indexing multiple levels of a MultiIndex

Looking up indexed data is fast and efficient. And you have already seen that lookups based on the outermost level of a MultiIndex work just like lookups on DataFrames that have a single-level Index.

Looking up data based on inner levels of a MultiIndex can be a bit trickier. The trickiest of all these lookups are when you want to access some inner levels of the index. In this case, you need to use slice(None) in the slicing parameter for the outermost dimension(s) instead of the usual :, or use pd.IndexSlice. You can refer to the pandas documentation for more details. For example, in the video, Dhavide used the following code to extract rows from all Symbols for the dates Oct. 3rd through 4th inclusive:

stocks.loc[(slice(None), slice('2016-10-03', '2016-10-04')), :]

Pay particular attention to the tuple (slice(None), slice('2016-10-03', '2016-10-04')).

In this exercise, you will use your sales DataFrame to do some increasingly complex lookups. Remember that you can type sales.head() in the console to review the structure of the DataFrame!

#Pivoting DataFrames

12/5/20 Time for a break! 
12/6/20 Completing dataframe work
12/7/20 - Completing dataframe work and working on trading program
12/8/20 - built a new automated data wrangler in python