const [package, setPackage] = useState({
    name: "",
    packageAmount: ""
    additionals: []
    addPrices: []
})

Selectbutton = fill in the name and the package amount into setPackage
Post request = sends data to backend for storing
Anytime the user visits this page either at first or returning setPackage
to default values

At checkout form basic information first
Then display prefilled selection for clarity
IE:
Package: ""
Additionals: ""
             ""
             ""
Total (maybe with breakdown?): 0000
Submit button