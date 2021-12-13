import cv2
import mediapipe as mp

def keypoint_extraction(input_path, output_path):
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    IMAGE_FILES = [input_path]
    with mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=2,
            min_detection_confidence=0.5) as hands:
        for idx, file in enumerate(IMAGE_FILES):
            image = cv2.flip(cv2.imread(file), 1)
            results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            if not results.multi_hand_landmarks:
                continue
            image_height, image_width, _ = image.shape
            annotated_image = image.copy()
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    annotated_image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
            cv2.imwrite(output_path, cv2.flip(annotated_image, 1))

