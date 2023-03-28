 <script type="text/javascript" charset="utf-8">
                    function httpPostAsync(method, params, callback) {
                        var xmlHttp = new XMLHttpRequest();
                        xmlHttp.onreadystatechange = function() { 
                            if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                                callback(xmlHttp.responseText);
                            else
                                callback(`Error ${xmlHttp.status}`)
                        }
                        xmlHttp.open("POST", window.location.href + method, true);
                        xmlHttp.setRequestHeader("Content-Type", "application/json");
                        xmlHttp.send(params);
                    }
                    
                    function ledOn() {
                        document.getElementById("textstatus").textContent = "Выключено";
                        httpPostAsync("led1", JSON.stringify({ "on": true }), function(resp) { 
                            document.getElementById("textstatus0").textContent = `Выключено`;
                        });
                    }

                    function ledOff() {
                        document.getElementById("textstatus").textContent = "Включено";
                        httpPostAsync("led1", JSON.stringify({ "on": false }), function(resp) { 
                            document.getElementById("textstatus").textContent = `Включено`;
                        });
                    }
                    
                    function ledOn1() {
                        document.getElementById("textstatus1").textContent = "Включено";
                        httpPostAsync("led2", JSON.stringify({ "on": true }), function(resp) { 
                            document.getElementById("textstatus1").textContent = `Выключено`;
                        });
                    }

                    function ledOff1() {
                        document.getElementById("textstatus1").textContent = "Выключено";
                        httpPostAsync("led2", JSON.stringify({ "on": false }), function(resp) { 
                            document.getElementById("textstatus1").textContent = `Включено`;
                        });
                    }
                    
                    function ledOn2() {
                        document.getElementById("textstatus2").textContent = "Включено";
                        httpPostAsync("led3", JSON.stringify({ "on": true }), function(resp) { 
                            document.getElementById("textstatus2").textContent = `Выключено`;
                        });
                    }

                    function ledOff2() {
                        document.getElementById("textstatus2").textContent = "Выключено";
                        httpPostAsync("led3", JSON.stringify({ "on": false }), function(resp) { 
                            document.getElementById("textstatus2").textContent = `Включено`;
                        });
                    }
                    function ledTime(){
                        document.getElementById("textstatus3").textContent =" ";
                        httpPostAsync("time", JSON.stringify({ "on":false }), function(resp) {
                            document.getElementById("textstatus3").textContent = ` `;
                            });
                    }
</script>                    
