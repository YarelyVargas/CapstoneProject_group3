import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass
    def makePredictions(self, BMI, PhysicalHealth, MentalHealth, Smoking, 
    AlcoholDrinking, Stroke, DiffWalking, Sex, PhysicalActivity, Asthma, KidneyDisease,SkinCancer,
     AgeCategory, Race, Diabetic, GenHealth ):

        AgeCat_18 = 0
        AgeCat_25 = 0
        AgeCat_30 = 0
        AgeCat_35 = 0
        AgeCat_40 = 0
        AgeCat_45 = 0
        AgeCat_50 = 0
        AgeCat_55 = 0
        AgeCat_60 = 0
        AgeCat_65 = 0
        AgeCat_70 = 0
        AgeCat_75 = 0
        AgeCat_80 = 0
        Race_w = 0
        Race_aa = 0
        Race_asi = 0
        Race_b = 0
        Race_h = 0
        Race_o = 0
        diabetic_n = 0
        diabetic_nbd = 0
        diabetic_y = 0
        diabetic_yp = 0
        gen_e=0
        gen_vg = 0
        gen_f = 0
        gen_g= 0
        gen_p = 0
        Smoking_n = 0 
        AlcoholDrinking_n = 0
        Stroke_n = 0
        DiffWalking_n = 0
        Sex_n = 0
        Asthma_n = 0
        KidneyDisease_n = 0
        SkinCancer_n = 0
        PhysicalActivity_n = 0

        # parse pclass
         # parse pclass

         # parse pclass

        if (GenHealth == 'Excellent'):
            gen_e = 1
        elif (GenHealth == 'Fair'):
            gen_f = 1
        elif (GenHealth == 'Good'):
            gen_g = 1
        elif (GenHealth == 'Poor'):
            gen_p = 1
        elif (GenHealth == 'Very good'):
            gen_vg = 1
        else:
            pass
            
        if (AgeCategory == '18-24'):
            AgeCat_18 = 1
        elif (AgeCategory == '25-29'):
            AgeCat_25 = 1
        elif (AgeCategory == '30-34'):
            AgeCat_30 = 1
        elif (AgeCategory == '35-39'):
            AgeCat_35 = 1
        elif (AgeCategory == '40-44'):
            AgeCat_40 = 1
        elif (AgeCategory == '45-49'):
            AgeCat_45 = 1
        elif (AgeCategory == '50-54'):
            AgeCat_50 = 1
        elif (AgeCategory == '55-59'):
            AgeCat_55 = 1
        elif (AgeCategory == '60-64'):
            AgeCat_60 = 1
        elif (AgeCategory == '65-69'):
            AgeCat_65 = 1
        elif (AgeCategory == '70-74'):
            AgeCat_70 = 1
        elif (AgeCategory == '75-79'):
            AgeCat_75 = 1
        elif (AgeCategory == '80 or older'):
            AgeCat_80 = 1
        else:
            pass

        if (Diabetic == 'No, borderline diabetes'):
            diabetic_nbd = 1
        elif (Diabetic == 'No'):
            diabetic_n = 1
        elif (Diabetic == 'Yes'):
            diabetic_y = 1
        elif (Diabetic == 'Yes (during pregnancy)'):
            diabetic_yp = 1
        else:
            pass

            

            
        if (Race == 'White'):
            Race_w = 1
        elif (Race == 'American Indian/Alaskan Native'):
            Race_aa = 1
        elif (Race == 'Asian'):
            Race_asi = 1
        elif (Race == 'Black'):
            Race_b = 1
        elif (Race == 'Hispanic'):
            Race_h = 1
        elif (Race == 'Other'):
            Race_o = 1
        else:
            pass

            
        if (Smoking == 'Yes'):
            Smoking_n = 1
        else: 
            pass

        if (AlcoholDrinking == 'Yes'):
            AlcoholDrinking_n = 1
        else: 
            pass

        if (Stroke == 'Yes'):
            Stroke_n = 1
        else: 
            pass

        if (DiffWalking == 'Yes'):
            DiffWalking_n = 1
        else: 
            pass

        if (Sex == 'Male'):
            Sex_n = 1
        else: 
            pass

        if (Asthma == 'Yes'):
            Asthma_n = 1
        else: 
            pass
        if (KidneyDisease == 'Yes'):
            KidneyDisease_n = 1
        else: 
            pass
        if (SkinCancer == 'Yes'):
            SkinCancer_n = 1
        else: 
            pass
        if (PhysicalActivity == 'Yes'):
            PhysicalActivity_n = 1
        else: 
            pass


        input_pred = [[BMI, PhysicalHealth, MentalHealth, Smoking_n, AlcoholDrinking_n,Stroke_n,DiffWalking_n,Sex_n,
               PhysicalActivity_n,Asthma_n,KidneyDisease_n,SkinCancer_n,AgeCat_18,AgeCat_25,
               AgeCat_30,AgeCat_35,AgeCat_40,AgeCat_45,AgeCat_50,AgeCat_55,AgeCat_60,AgeCat_65, AgeCat_70,
              AgeCat_75,AgeCat_80,Race_aa,Race_asi,Race_b,Race_h,Race_o,Race_w,diabetic_n,
               diabetic_nbd,diabetic_y,diabetic_yp,gen_e,gen_f,gen_g,gen_p,gen_vg]]


        filename = 'finalized_model_us.sav'
        Rforest_load = pickle.load(open(filename, 'rb'))
        X = np.array(input_pred)
        # preds = Rforest_load.predict_proba(X)
        preds_singular = Rforest_load.predict(X)

        return preds_singular[0]

