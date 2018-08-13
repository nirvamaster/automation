'start a new subroutine called SearchBot
Sub SearchBot()

    'dimension (declare or set aside memory for) our variables
    Dim objIE As InternetExplorer 'special object variable representing the IE browser
    Dim aEle As HTMLLinkElement 'special object variable for an <a> (link) element
    Dim y As Integer 'integer variable we'll use as a counter
    'Dim result As String 'string variable that will hold our result link
    Dim Name As String
    Dim Position As String
    Dim Location As String
    Dim Url
    Dim Snippet


    'initiating a new instance of Internet Explorer and asigning it to objIE
    Set objIE = New InternetExplorer

    'make IE browser visible (False would allow IE to run in the background)
    objIE.Visible = True
 For i = 1 To 40
    'navigate IE to this web page (a pretty neat search engine really)
    objIE.navigate "https://www.linkedin.com/search/results/people/?company=&facetCurrentCompany=%5B%22%22%5D&facetGeoRegion=%5B%22us%3A70%22%5D&firstName=&lastName=&origin=FACETED_SEARCH&page=" & i & "&school=&title="
   'wait here a few seconds while the browser is busy
    Do While objIE.Busy = True Or objIE.readyState <> 4: DoEvents: Loop
    objIE.document.parentWindow.scrollBy 0, 200
    objIE.document.parentWindow.scrollBy 0, 400
    objIE.document.parentWindow.scrollBy 0, 600
    objIE.document.parentWindow.scrollBy 0, 800
    objIE.document.parentWindow.scrollBy 0, 1000

    random = Int(4 * Rnd)
    Application.Wait (Now + TimeValue("0:00:" & random))

    'the first search result will go in row 2
    y = 10 * i

    'for each <a> element in the collection of objects with class of 'result__a'...
    For Each aEle In objIE.document.getElementsByClassName("search-result__wrapper")

        Name = Trim(aEle.getElementsByClassName("actor-name")(0).innerText)
        Position = Trim(aEle.getElementsByClassName("subline-level-1")(0).innerText)
        Location = Trim(aEle.getElementsByClassName("subline-level-2")(0).innerText)
        Url = Trim(aEle.getElementsByClassName("search-result__result-link")(0).getAttribute("href"))
        If aEle.getElementsByClassName("search-result__snippets")(0) Is Nothing Then
        Snippet = "None"
        Else
        Snippet = Trim(aEle.getElementsByClassName("search-result__snippets")(0).innerText)
        End If
        '...get the text within the element and print it to the sheet in col D
        Sheets("IE").Range("B" & y).Value = Name
        Sheets("IE").Range("C" & y).Value = Position
        Sheets("IE").Range("D" & y).Value = Location
        Sheets("IE").Range("E" & y).Value = Url
        Sheets("IE").Range("F" & y).Value = Snippet

        Debug.Print Name
        Debug.Print Position
        Debug.Print Location
        Debug.Print Url
        Debug.Print Snippet

        'increment our row counter, so the next result goes below
        y = y + 1

    'repeat times the # of ele's we have in the collection
    Next

    random = Int(4 * Rnd)
    Application.Wait (Now + TimeValue("0:00:" & random))

  Next i

    'close the browser
    objIE.Quit

'exit our SearchBot subroutine
End Sub
