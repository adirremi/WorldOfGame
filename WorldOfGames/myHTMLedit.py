def god_html(score):
    html = """\
        <html>

            <head>
            <title>Scores Game</title>
            </head>
            <body>
              <h1>Welcome to the WorldOFGame!
              The score is <div id="Score">{score}</div></h1>
            </body>
        </html>
        """.format(score=score)
    return html


def bad_html():
    html = """\
            <html>

                <head>
                <title>Scores Game</title>
                </head>
                <body>
                  <h1><div id="score" style="color:red">{ERROR}</div></h1>
                </body>
            </html>
            """
    return html


def ranktable(top3list):
    ranklist = top3list
    html = """<HTML>
    <body>
        <h1>Welcome To WorldOfGame</h1>
    <TABLE BORDER="5"    WIDTH="50%"   CELLPADDING="4" CELLSPACING="3">
   <TR>
      <TH COLSPAN="2"><BR><H3>Ranking List</H3>
      </TH>
   </TR>
   <TR>
      <TH>NickName</TH>
      <TH>Points</TH>
   </TR>
   <TR ALIGN="CENTER">
      <TD>{ranklist[0][0]}</TD>
      <TD>{ranklist[0][1]}</TD>
      </TR>
   <TR ALIGN="CENTER">
      <TD>{ranklist[1][0]}</TD>
      <TD>{ranklist[1][1]}</TD>
   </TR>
   <TR ALIGN="CENTER">
      <TD>{ranklist[2][0]}</TD>
      <TD>{ranklist[2][1]}</TD>
   </TR>
   
</TABLE>

        
    </body>
    </HTML>""".format(**locals())
    return html
