class DiseaseDiagnosisSystem:
    def __init__(self):
        # Expanded Knowledge Base: 10 diseases with symptoms and severity considerations
        self.knowledge_base = {
            'Influenza': {
                'symptoms': ['fever', 'cough', 'sore throat', 'muscle aches', 'fatigue', 'headache', 'chills'],
                'required_matches': 4
            },
            'Common Cold': {
                'symptoms': ['runny nose', 'sneezing', 'sore throat', 'mild cough', 'congestion', 'mild fatigue'],
                'required_matches': 3
            },
            'Strep Throat': {
                'symptoms': ['severe sore throat', 'difficulty swallowing', 'fever', 'swollen lymph nodes', 'white patches on tonsils'],
                'required_matches': 3
            },
            'Gastroenteritis': {
                'symptoms': ['nausea', 'vomiting', 'diarrhea', 'abdominal cramps', 'fever', 'dehydration'],
                'required_matches': 3
            },
            'Migraine': {
                'symptoms': ['severe headache', 'nausea', 'sensitivity to light', 'sensitivity to sound', 'visual disturbances', 'dizziness'],
                'required_matches': 3
            },
            'Pneumonia': {
                'symptoms': ['high fever', 'productive cough', 'chest pain', 'shortness of breath', 'fatigue', 'chills'],
                'required_matches': 4
            },
            'Sinusitis': {
                'symptoms': ['facial pain', 'nasal congestion', 'thick nasal discharge', 'headache', 'fever', 'reduced sense of smell'],
                'required_matches': 3
            },
            'Bronchitis': {
                'symptoms': ['persistent cough', 'mucus production', 'wheezing', 'chest discomfort', 'fatigue', 'low fever'],
                'required_matches': 3
            },
            'Allergic Rhinitis': {
                'symptoms': ['sneezing', 'itchy eyes', 'runny nose', 'nasal congestion', 'itchy throat', 'watery eyes'],
                'required_matches': 3
            },
            'Tension Headache': {
                'symptoms': ['mild headache', 'tight band around head', 'neck stiffness', 'shoulder stiffness', 'fatigue'],
                'required_matches': 3
            }
        }
        
        # Comprehensive symptom list
        self.all_symptoms = sorted(set(
            symptom for disease in self.knowledge_base.values() 
            for symptom in disease['symptoms']
        ))
        
        # History to track previous diagnoses
        self.diagnosis_history = []

    def display_symptoms(self):
        """Display all possible symptoms with numbers for selection"""
        print("\nAvailable Symptoms:")
        for i, symptom in enumerate(self.all_symptoms, 1):
            print(f"{i}. {symptom}")

    def get_user_symptoms(self):
        """Get symptoms and their severity from user input"""
        self.display_symptoms()
        print("\nInstructions: Enter symptom numbers followed by severity (1-3) where 1=mild, 2=moderate, 3=severe")
        print("Example: '1:2 3:1' for symptom 1 (moderate) and symptom 3 (mild)")
        
        while True:
            try:
                selections = input("\nEnter your symptoms with severity (e.g., '1:2 3:1'): ").strip().split()
                user_symptoms = {}
                for selection in selections:
                    num, severity = selection.split(':')
                    num, severity = int(num), int(severity)
                    if 1 <= num <= len(self.all_symptoms) and 1 <= severity <= 3:
                        symptom = self.all_symptoms[num-1]
                        user_symptoms[symptom] = severity
                    else:
                        print(f"Invalid input: {selection}")
                        return None
                return user_symptoms if user_symptoms else None
            except (ValueError, IndexError):
                print("Invalid format. Use 'number:severity' (e.g., '1:2') with numbers separated by spaces.")
                return None

    def diagnose(self, user_symptoms):
        """Enhanced inference mechanism considering symptom severity"""
        if not user_symptoms:
            return "Unable to diagnose due to invalid input"

        possible_diagnoses = []
        
        for disease, info in self.knowledge_base.items():
            matching_symptoms = set(user_symptoms.keys()) & set(info['symptoms'])
            match_count = len(matching_symptoms)
            
            # Calculate weighted score based on severity
            severity_score = sum(user_symptoms[sym] for sym in matching_symptoms) if matching_symptoms else 0
            total_possible_severity = len(info['symptoms']) * 3  # Max severity is 3 per symptom
            confidence = (severity_score / total_possible_severity) * 100 if total_possible_severity else 0
            
            if match_count >= info['required_matches']:
                possible_diagnoses.append({
                    'disease': disease,
                    'confidence': confidence,
                    'matched_symptoms': list(matching_symptoms),
                    'severity_score': severity_score
                })
            elif match_count > 0:  # Partial match for feedback
                possible_diagnoses.append({
                    'disease': disease,
                    'confidence': confidence,
                    'matched_symptoms': list(matching_symptoms),
                    'severity_score': severity_score,
                    'partial': True
                })

        # Sort by confidence, prioritizing full matches
        possible_diagnoses.sort(key=lambda x: (not x.get('partial', False), x['confidence']), reverse=True)
        return possible_diagnoses

    def display_diagnosis(self, diagnoses):
        """Display detailed diagnosis results"""
        if not diagnoses:
            print("\nNo matching diagnosis found based on the provided symptoms.")
            print("Please consult a healthcare professional for proper evaluation.")
            return

        if isinstance(diagnoses, str):
            print(f"\n{diagnoses}")
            return

        print("\nPossible Diagnoses (sorted by likelihood):")
        for diag in diagnoses:
            status = "(Partial Match)" if diag.get('partial') else "(Full Match)"
            print(f"\nDiagnosis: {diag['disease']} {status}")
            print(f"Confidence: {diag['confidence']:.1f}%")
            print(f"Matched Symptoms: {', '.join(diag['matched_symptoms'])}")
            print(f"Severity Score: {diag['severity_score']}")
        
        print("\nNote: This is an AI-based estimation, not a professional medical diagnosis.")
        print("Please consult a doctor for accurate assessment and treatment.")

    def show_history(self):
        """Display diagnosis history"""
        if not self.diagnosis_history:
            print("\nNo diagnosis history available.")
        else:
            print("\nDiagnosis History:")
            for i, entry in enumerate(self.diagnosis_history, 1):
                print(f"{i}. {entry}")

    def run(self):
        """Main loop with expanded functionality"""
        print("Welcome to the Enhanced AI Disease Diagnosis System")
        print("==================================================")
        
        while True:
            print("\nOptions:")
            print("1. Diagnose symptoms")
            print("2. View diagnosis history")
            print("3. Exit")
            
            choice = input("Select an option (1-3): ").strip()
            
            if choice == '1':
                symptoms = self.get_user_symptoms()
                if symptoms:
                    diagnosis = self.diagnose(symptoms)
                    self.display_diagnosis(diagnosis)
                    if isinstance(diagnosis, list) and diagnosis:
                        history_entry = f"Symptoms: {symptoms} -> Top Diagnosis: {diagnosis[0]['disease']} ({diagnosis[0]['confidence']:.1f}%)"
                        self.diagnosis_history.append(history_entry)
            elif choice == '2':
                self.show_history()
            elif choice == '3':
                print("Thank you for using the Diagnosis System. Stay healthy!")
                break
            else:
                print("Invalid option. Please select 1, 2, or 3.")


# Run the system
if __name__ == "__main__":
    system = DiseaseDiagnosisSystem()
    system.run()
