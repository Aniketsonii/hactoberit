let traverse_json = function(key, value) {
  for (let i in key) {
    fn.apply(this,[i,key[i]]);  
    if (key[i] !== null && typeof(key[i])=="object") {
      traverse_json(key[i], value);
    }
  }
}

// usage
var obj = {};
traverse(obj, function(k,v){
  console.log(k + " : " + v);
});
