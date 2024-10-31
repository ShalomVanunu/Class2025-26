function __CreatePopupCallBack(parameters,context){
    var popup = window.open();
    var array = parameters.split(";");
    if (array.length > 0) {
    
        popup.document.write("<HTML><BODY><FORM runat='server' method='POST' action='" + array[0] + "'>");
        if (array.length > 1) {
            popup.document.write(array[1]);
            popup.document.write("</FORM></BODY></HTML>");
            popup.document.forms(0).submit();
        }
    }
}

function __CreatePopupCallBackError(parameters,context){
    window.alert("Error: failed to prepare parameters!");
}

var wwPopBlank = "";
var __pp_popup = null;
var __pp_url = null;
var __pp_formid = null;
var __pp_names = null;
var __pp_values = null;
var __pp_parameters = null;
var __pp_content = null;

function __CreatePopupWindow(url , formId , names, values, parameters ){
    __CreatePopupWindow(url , formId , names, values, parameters, null );
}

function __CreatePopupWindow(url , formId , names, values, parameters, content ){
    
    __pp_popup = window.open(wwPopBlank,"",parameters);

    __pp_url = url;
    __pp_formid = formId;
    __pp_names = names;
    __pp_values = values;
    __pp_parameters = parameters;
    __pp_content = content;

    contentTimer = window.setTimeout("__WritePopupContent()", 500);
}

function __WritePopupContent()
{    
    try
    {
        clearTimeout(contentTimer);
        //window.status = "__WritePopupContent()";

        if (__pp_popup == null)
        {
            contentTimer = window.setTimeout("__WritePopupContent()", 500);
        }
        else
        {
            //window.status = "__pp_popup is not null";
            
            clearTimeout(contentTimer);
            contentTimer = 0;
            
            //window.status = "writing content to __pp_popup";
            
            __pp_popup.document.write("<HTML><HEAD>");
            __pp_popup.document.write("<TITLE>אנא המתן</TITLE>");
            __pp_popup.document.write("<link href='../../App_Themes/Green/default.css' type='text/css' rel='Stylesheet' />");
            __pp_popup.document.write("</HEAD><BODY>");
            
            // call a function to add header text
            __pp_popup.document.write(__pp_content == null ? __getPopUpHeader(__pp_popup) : __pp_content);
            //__pp_popup.document.write("<span class='PleaseWaitMessage'>אנא המתן</span>")
            
            // call a function to add footer text
            __pp_popup.document.write(__getPopUpFooter(__pp_popup));
            __pp_popup.document.write("<FORM id='frm1' method='POST' action='" + __pp_url + "'>");
            
            var form =  window.document.getElementById(__pp_formid);
                    
            //window.status = "got the form instance...";                
                    
            // take form object from hierarchy
            if (form.tagName.toLowerCase() != "form") 
            {
                while(form && form.tagName.toLowerCase() != "form") form = form.parentNode;
            }
            if (form) 
            {
                //window.status = "wrirting form elements.. before submitting...";
                for(var i = 0; i < __pp_names.length; i++)
                {                
                    try 
                    {
                       __pp_popup.document.write("<INPUT type='hidden' name='__param_" + __pp_names[i] + "' value='" + ((__pp_values) ? __pp_values[i] : form.elements(__pp_names[i]).value) + "' />");
                    }
                    catch(e){}
                }  
            }
                    
            __pp_popup.document.write("</FORM></BODY></HTML>");                
            
            //window.status = "going to submit function";
            
            setTimeout("submitFunc()", 500);                        
            
            //window.status = "type of form is " + typeof(form) + "  ::  form ul is : " + __pp_url;
            
            return __pp_popup;
        }
    }
    catch(e){window.status = "ERROR : " + e.description}
}

function submitFunc()
{        
    //window.status = "going to submit function";
    __pp_popup.document.forms[0].submit();
}
