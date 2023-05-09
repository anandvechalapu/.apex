public class RenewalNoticeTrigger{

public static void triggerRenewalNotice(){

// Set the Renewal Notice Trigger Limit & Frequency
Integer renewalNoticeTriggerLimit = 90;
String renewalNoticeTriggerFrequency = 'days';

// Set the target date example
Date targetDateExample = Date.newInstance(2019,12,1);

// Get the Annual Renewal Date
Date annualRenewalDate = Date.newInstance(Date.today().year(), 12, 1); 

// Calculate the renewal notice trigger date
Date renewalNoticeTriggerDate = annualRenewalDate.addDays(-renewalNoticeTriggerLimit);

// Check if the renewal notice trigger date is equal to the target date example
if(renewalNoticeTriggerDate == targetDateExample){

// Trigger the renewal notice
System.debug('Renewal Notice triggered!');

}

}

}